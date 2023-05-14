### 🔴 Ćwiczenie

# Zerknij na rozwiązanie ćwiczenia M04L08. Znajduje się tam trochę powtórzonego kodu.
# 1. Użyj funkcji, aby uniknąć duplikacji kodu.
# 2. Popraw kod tak, aby miał funkcję main().
# 3. Czy widzisz jakieś bloki kodu zaczynające się od komentarza podsumowującego, co robi dany blok? Jeśli tak, to jak możesz zwiększyć czytelność kodu poprzez wprowadzenie nowych funkcji?

import glob
import string

def get_comment ():
    text= input("Please write a comment: ").lower()
    # if not text:
    #     print("No comment to measure")
    #     quit()
    return text

def open_files(file_pattern):
    files = glob.glob(file_pattern)
    contents = []
    for file in files:
        with open(file) as stream:
            content = stream.read()
            contents.append(content)
    return contents

def clean_text(text):
    content= text.replace("<br />", " ").lower().strip(PUNCTUATION)
    comments= content.split()     
        list_positives.append(comments)
    return list_positives
# print(list_positives)
     
list_negatives= []
for file in files_negative:
    with open(file) as stream:
        content= stream.read()
        content= content.replace("<br />", " ").lower().strip(PUNCTUATION)
        comments= content.split()
        list_negatives.append(comments)
    return list_negatives
# print(list_negatives)

counter_positive= 0
counter_negative= 0

all_words_sentiment= []
words_not_found= []

def delete_punctuation(text):
    words= text.split()
    for word in words:
        word= word.strip(PUNCTUATION)
    return word
    
def conuter_words(word, list_???):    
        for comment in list_positives:
            if word in comment:
                counter_positive+= 1
        positive= counter_positive
        counter_positive = 0   
        for comment in list_negatives:
            if word in comment:
                counter_negative+= 1
        negative= counter_negative
        counter_negative = 0 
    return counter ????????/ # jak połączyć pozyt i negat 

    # print("Word:", word, "Found in positive comments:", positive, "Found in negative comments:", negative)     
    
# FILENAME_POSITIVE = "/Users/ilo/Desktop/PYTHON/do cwiczenia/pozytywne/*"
# FILENAME_NEGATIVE= "/Users/ilo/Desktop/PYTHON/do cwiczenia/negatywne/*"

FILENAME_POSITIVE= "Praktyczny_Python_materialy-2022-08-23/M03/data/aclImdb/train/pos/*"
FILENAME_NEGATIVE= "Praktyczny_Python_materialy-2022-08-23/M03/data/aclImdb/train/neg/*"
PUNCTUATION= string.punctuation

files_positive= glob.glob(FILENAME_POSITIVE)
files_negative= glob.glob(FILENAME_NEGATIVE)

    all_= positive + negative

    if all_ > 0:
        word_sentiment= (positive - negative)/ all_
        all_words_sentiment.append(word_sentiment)
        print( word, "sentiment:", word_sentiment)  
    else:
        words_not_found.append(word)

if len(all_words_sentiment) == 0:
        print("Not enough data to measure your comment")
else:
    text_sentiment= sum(all_words_sentiment) / len(all_words_sentiment)
    if text_sentiment > 0:
        print("")
        print("This comment is positive")
        print("It's sentiment:", text_sentiment)
    else:
        print("")
        print("This comment is negative")
        print("It's sentiment:", text_sentiment)
    
    if len(words_not_found) > 0:
        print("")
        print("[WARNING] Some words cannot be measured:", " ".join(words_not_found))


def main(TBD):
    # 1. najpierw pobranie tekstu od uzytkownika
        get_text_from_user()
    # 2. sprzatanie tekstu od uzytkownika
        cleanup_user_input()
    # 3. zbuduj baze wiedzy na podstawie pozytywnych i negatywnych
        slurp_database()
    # 4. dla kazdego slowa z danych uzytkownika policz wystapienia w bazie wiedzy (dla pozytywnych i negatywnych oddzielnie)
    # 5. policz sentyment
    # 6. wyswietl uytkownikowi wynik

if __name__ == "__main__":
    main()
