# Pomóż zespołowi Stanford AI Lab przeanalizować zbiór danych składający się z 50 tys. recenzji filmów, dzięki czemu będą mogli automatycznie określać sentyment nowych komentarzy i wypowiedzi w internecie. W szczególności zależy im, aby zidentyfikować te najbardziej pozytywne i negatywne wypowiedzi wśród milionów neutralnych komentarzy - dzięki temu będą mogli udostępnić te najbardziej pozytywne, a w przypadku tych najbardziej negatywnych będą mogli zareagować i odpowiedzieć zanim taki komentarz dotrze do szerszego grona.

# 1. Wszystkie pliki znajdują się w katalogu M03/data/aclImdb/train. W podkatalogu "pos" znajdują się pozytywne komentarze, tzn. minimum 7/10. W podkatalogu "neg" znajdują się negatywne komentarze, czyli te 6/10, 5/10 i niżej. Każda recenzja to osobny plik.
# 2. W recenzjach znajdują się fragmenty HTML - "<br />" oznaczający znak końca linii. Takie fragmenty zastąp spacją.
# 3. Wczytaj wszystkie pozytywne i negatywne recenzje do dwóch osobnych zmiennych. Będzie łatwiej, jeśli każdą recenzję będziesz reprezentować nie jako string, tylko jako listę słów. Tak więc każda z tych dwóch osobnych zmiennych będzie listą list.
# 4. Następnie poproś użytkownika, aby wpisał komentarz, którego sentyment chce wyliczyć. Podziel ten komentarz na słowa.
# 5. Sentyment poszczególnych słów w tym komentarzu liczymy wg wzoru (positive-negative)/all_, gdzie positive to liczba pozytywnych recenzji, w których pojawiło się to słowo. Negative to liczba negatywnych recenzji, w których pojawiło się to słowo. Natomiast all_ to liczba wszystkich recenzji, w których pojawiło się to słowo. Na przykład, jeśli dane słowo pojawia się w 5 pozytywnych i 5 negatywnych recenzjach, to jego sentyment wynosi (5-5)/10 = 0.0. Jeśli dane słowo pojawia się w 9 pozytywnych i 1 negatywnej recenzji, to jego sentyment wynosi (9-1)/10 = +0.8. Jeśli dane słowo pojawia się w 90 pozytywnych i 10 negatywnych recenzjach, to jego sentyment wynosi (90-10)/100 = +0.8, tak samo jak wcześniej. Tak więc liczba zawsze jest z zakresu od -1.0 do +1.0. 
# 6. Sentyment całego tego komentarza to średnia arytmetyczna sentymentu wszystkich słów. Tak więc wystarczy zsumować sentyment poszczególnych słów i następnie taką sumę podzielić przez liczbę słów. W ten sposób sentyment całego komentarza też będzie z zakresu od -1.0 do +1.0.
# 7. Cały komentarz uznajemy za pozytywny, gdy jego sentyment jest > 0, a negatywny gdy jest < 0.

# negative- positive /all - sentiment

import glob
import string

FILENAME_POSITIVE= "Praktyczny_Python_materialy-2022-08-23/M03/data/aclImdb/train/pos/*"
FILENAME_NEGATIVE= "Praktyczny_Python_materialy-2022-08-23/M03/data/aclImdb/train/neg/*"
PUNCTUATION= string.punctuation

# FILENAME_POSITIVE = "/Users/ilo/Desktop/PYTHON/do cwiczenia/pozytywne/*"
# FILENAME_NEGATIVE= "/Users/ilo/Desktop/PYTHON/do cwiczenia/negatywne/*"

files_positive= glob.glob(FILENAME_POSITIVE)
files_negative= glob.glob(FILENAME_NEGATIVE)

text= input("Please write a comment: ").lower()
if not text:
    print("No comment to measure")
    quit()

list_positives= []
for file in files_positive:
    with open(file) as stream:
        content= stream.read()
        content= content.replace("<br />", " ").lower().strip(PUNCTUATION)
        comments= content.split()     
        list_positives.append(comments)
# print(list_positives)
     
list_negatives= []
for file in files_negative:
    with open(file) as stream:
        content= stream.read()
        content= content.replace("<br />", " ").lower().strip(PUNCTUATION)
        comments= content.split()
        list_negatives.append(comments)
# print(list_negatives)

counter_positive= 0
counter_negative= 0

all_words_sentiment= []
words_not_found= []

words= text.split()
for word in words:
    word= word.strip(PUNCTUATION)
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

    # print("Word:", word, "Found in positive comments:", positive, "Found in negative comments:", negative)     
    
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
