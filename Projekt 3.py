### 🔴 Ćwiczenie

# Zerknij na rozwiązanie ćwiczenia M04L08. Znajduje się tam trochę powtórzonego kodu.
# 1. Użyj funkcji, aby uniknąć duplikacji kodu.
# 2. Popraw kod tak, aby miał funkcję main().
# 3. Czy widzisz jakieś bloki kodu zaczynające się od komentarza podsumowującego, co robi dany blok? Jeśli tak, to jak możesz zwiększyć czytelność kodu poprzez wprowadzenie nowych funkcji?

import glob
import string
from typing import List, Union

def get_user_text () -> str:
    text= input("Please write a comment: ").lower()
    # if not text:
    #     print("No comment to measure")
    #     quit()
    return text

def cleanup_user_input(text:str) -> list:
    PUNCTUATION= string.punctuation
    cleaned_words= []
    content= text.replace("<br />", " ").lower()
    words= content.split()
    for word in words:
        word= word.strip(PUNCTUATION)     
        cleaned_words.append(word)
    return cleaned_words

def open_files(file_pattern: str) -> List[str]:
    files = glob.glob(file_pattern)
    list_comments = []
    for file in files:
        with open(file) as stream:
            content = stream.read()
            list_comments.append(content)
    return list_comments

def count_word_occurrences(word: str, comments: List[str]) -> int:
    counter = 0
    for comment in comments:
        if word in comment:
            counter += 1
    return counter
      
def calculate_word_sentiment(positive_count: int, negative_count: int) -> Union[float, None]:
    all_ = positive_count + negative_count

    if all_ > 0:
        word_sentiment = (positive_count - negative_count) / all_
    else:
        word_sentiment = None
    return word_sentiment

def calculate_comment_sentiment(words_sentiment: List[float]) -> float:
    comment_sentiment = sum(words_sentiment) / len(words_sentiment)
    return comment_sentiment

def display_sentiment(comment_sentiment: float, words_not_found: List[str]):
    if comment_sentiment > 0:
        print("")
        print("This comment is positive")
        print("It's sentiment:", comment_sentiment)
    else:
        print("")
        print("This comment is negative")
        print("It's sentiment:", comment_sentiment)
    
    if len(words_not_found) > 0:
        print("")
        print("[WARNING] Some words cannot be measured:", " ".join(words_not_found))

def main() -> None:
    FILENAME_POSITIVE = "Praktyczny_Python/M03/data/aclImdb/train/pos/*"
    FILENAME_NEGATIVE = "Praktyczny_Python/M03/data/aclImdb/train/neg/*"
    # 1. najpierw pobranie tekstu od uzytkownika
    user_text = get_user_text()
    # 2. sprzatanie tekstu od uzytkownika
    cleaned_user_text = cleanup_user_input(user_text)
     # 3. zbuduj baze wiedzy na podstawie pozytywnych i negatywnych
    positive_comments = open_files(FILENAME_POSITIVE)
    negative_comments = open_files(FILENAME_NEGATIVE)

    # 4. dla kazdego slowa z danych uzytkownika policz wystapienia w bazie wiedzy (dla pozytywnych i negatywnych oddzielnie)

    words_sentiment = []
    words_not_found = []
    for word in cleaned_user_text:
        positive_count = count_word_occurrences(word, positive_comments)
        negative_count = count_word_occurrences(word, negative_comments)
        # 5. policz sentyment kadego słowa
        word_sentiment = calculate_word_sentiment(positive_count, negative_count)
        # 6. policz sentyment całego komentarza
        if word_sentiment != None:
            words_sentiment.append(word_sentiment) 
        else:
            words_not_found.append(word)

    comment_sentiment = calculate_comment_sentiment(words_sentiment)
    # 7. wyświetl uzytkownikowi wynik
    display_sentiment(comment_sentiment, words_not_found)

if __name__ == '__main__':
    main()
