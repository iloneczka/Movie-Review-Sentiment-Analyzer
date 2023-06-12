"""
Sentiment Analysis of Movie Reviews

This script helps the Stanford AI Lab team analyze a dataset consisting of 50,000 movie reviews, allowing them to automatically determine the sentiment of new comments and online statements. The goal is to identify the most positive and negative expressions among millions of neutral comments, enabling the team to highlight the most positive ones and respond to the most negative ones before they reach a wider audience.

The script performs the following steps:

1. All files are located in the directory "M03/data/aclImdb/train." The "pos" subdirectory contains positive comments, which are rated at least 7/10. The "neg" subdirectory contains negative comments, rated 6/10, 5/10, and below. Each review is stored as a separate file.

2. The reviews may contain HTML fragments, such as "<br />" indicating line breaks. Replace these fragments with spaces.

3. Load all positive and negative reviews into two separate variables. It is easier to represent each review as a list of words instead of a string. Therefore, each variable will be a list of lists.

4. Prompt the user to enter a comment for which they want to calculate the sentiment. Split this comment into words.

5. Calculate the sentiment of each word in the comment using the formula (positive - negative) / all_, where "positive" is the number of positive reviews containing the word, "negative" is the number of negative reviews containing the word, and "all_" is the total number of reviews containing the word. For example, if a word appears in 5 positive and 5 negative reviews, its sentiment is (5 - 5) / 10 = 0.0. If a word appears in 9 positive and 1 negative review, its sentiment is (9 - 1) / 10 = +0.8. If a word appears in 90 positive and 10 negative reviews, its sentiment is (90 - 10) / 100 = +0.8, as before. Therefore, the sentiment value always falls within the range of -1.0 to +1.0.

6. The sentiment of the entire comment is the arithmetic mean of the sentiments of all the words. Therefore, sum up the sentiments of each word and divide the sum by the total number of words. This way, the sentiment of the entire comment will also fall within the range of -1.0 to +1.0.

7. The entire comment is considered positive if its sentiment is > 0 and negative if it is < 0.

"""

import glob
import string
from typing import List, Union

def get_user_text() -> str:
    """
    Prompts the user to write a comment and returns the entered text.

    Returns:
        str: The user-entered text.

    Raises:
        SystemExit: If no comment is entered, the program is terminated.

    """
    text= input("Please write a comment: ")
    if not text:
        print("No comment to measure")
        quit()
    return text

def cleanup_user_input(text:str) -> list:
    """
    Cleans the given text by removing punctuation and converting it to lowercase.

    Arguments:
        text (str): The input text to be cleaned.

    Returns:
        list: A list of cleaned words.

    """
    PUNCTUATION= string.punctuation
    cleaned_words= []
    content= text.replace("<br />", " ").lower()
    words= content.split()
    for word in words:
        word= word.strip(PUNCTUATION)     
        cleaned_words.append(word)
    return cleaned_words

def open_files(file_pattern: str) -> List[str]:
    """
    Opens files matching the given file pattern and returns a list of their contents.

    Arguments:
        file_pattern (str)

    Returns:
        List[str]: A list containing the contents of the matched files.

    """
    files = glob.glob(file_pattern)
    list_comments = []
    for file in files:
        with open(file) as stream:
            content = stream.read()
            list_comments.append(content)
    return list_comments

def count_word_occurrences(word: str, comments: List[str]) -> int:
    """
    Counts the occurrences of a word in a list of comments.

    Arguments:
        word (str): The word to count.
        comments (List[str]): The list of comments to search in.

    Returns:
        int: The number of occurrences of the word in the comments.

    """
    counter = 0
    for comment in comments:
        if word in comment:
            counter += 1
    return counter
      
def calculate_word_sentiment(positive_count: int, negative_count: int) -> Union[float, None]:
    """
    Calculates the sentiment of a word based on the counts of positive and negative occurrences.

    Argmentss:
        positive_count (int): The count of positive occurrences of the word.
        negative_count (int): The count of negative occurrences of the word.

    Returns:
        Union[float, None]: The calculated sentiment of the word as a float, or None if the counts are zero.

    """
    all_ = positive_count + negative_count

    if all_ > 0:
        word_sentiment = (positive_count - negative_count) / all_
    else:
        word_sentiment = None
    return word_sentiment

def calculate_comment_sentiment(words_sentiment: List[float]) -> float:
    """
    Calculates the sentiment of a comment based on the sentiments of its words.

    Args:
        words_sentiment (List[float]): The list of word sentiments.

    Returns:
        float: The calculated sentiment of the comment.

    """
    comment_sentiment = sum(words_sentiment) / len(words_sentiment)
    return comment_sentiment

def display_sentiment(comment_sentiment: float, words_not_found: List[str]):
    """
    Displays the sentiment of a comment and any words that could not be measured.

    Arguments:
        comment_sentiment (float): The sentiment of the comment.
        words_not_found (List[str]): The list of words that could not be measured.

    """
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
    """
    The main function that runs the sentiment analysis program.

    """
    FILENAME_POSITIVE = "Praktyczny_Python/M03/data/aclImdb/train/pos/*"
    FILENAME_NEGATIVE = "Praktyczny_Python/M03/data/aclImdb/train/neg/*"
    # 1. Prompt the user to enter a comment
    user_text = get_user_text()
    # 2. Clean up the user's input
    cleaned_user_text = cleanup_user_input(user_text)
    # 3. Open positive and negative comments files
    positive_comments = open_files(FILENAME_POSITIVE)
    negative_comments = open_files(FILENAME_NEGATIVE)

    # 4. Count word occurrences in positive and negative comments
    words_sentiment = []
    words_not_found = []
    for word in cleaned_user_text:
        positive_count = count_word_occurrences(word, positive_comments)
        negative_count = count_word_occurrences(word, negative_comments)
        # 5. Calculate sentiment for each word
        word_sentiment = calculate_word_sentiment(positive_count, negative_count)
        # 6. Calculate sentiment for the whole comment
        if word_sentiment is not None:
            words_sentiment.append(word_sentiment)
        else:
            words_not_found.append(word)

    comment_sentiment = calculate_comment_sentiment(words_sentiment)
    # 7. Display the sentiment to the user
    display_sentiment(comment_sentiment, words_not_found)

if __name__ == '__main__':
    main()
