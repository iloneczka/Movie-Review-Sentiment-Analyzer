"""
Sentiment Analysis of Movie Reviews

This script helps to analyze a dataset consisting of 50,000 movie reviews, allowing them to automatically determine the sentiment of new comments and online statements. The goal is to identify the most positive and negative expressions among millions of neutral comments, enabling the team to highlight the most positive ones and respond to the most negative ones before they reach a wider audience.

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
    text = input("Please write a comment: ")
    if not text:
        print("No comment to measure")
        quit()
    return text

def cleanup_user_input(text: str) -> List[str]:
    """
    Cleans the given text by removing punctuation and converting it to lowercase.

    Arguments:
        text (str): The input text to be cleaned.

    Returns:
        List[str]: A list of cleaned words.

    """
    PUNCTUATION = string.punctuation
    cleaned_words = []
    content = text.replace("<br />", " ").replace("<br/>", " ").lower()
    words = content.split()
    for word in words:
        word = word.strip(PUNCTUATION)
        cleaned_words.append(word)
    return cleaned_words

def open_files(file_pattern: str) -> List[str]:
    """
    Opens files matching the given file pattern and returns a list of their contents.

    Arguments:
        file_pattern (str): The pattern to match the file names.

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

    Arguments:
        positive_count (int): The count of positive occurrences of the word.
        negative_count (int): The count of negative occurrences of the word.

    Returns:
        Union[float, None]: The calculated sentiment of the word as a float, or None if the counts are zero.

    """
    all_ = positive_count + negative_count

    if all_ > 0:
        word_sentiment = (positive_count - negative_count) / all_
    else:
        word_sentiment = 0
    return word_sentiment

def calculate_comment_sentiment(word_sentiment: List[float]) -> float:
    """
    Calculates the sentiment of a comment based on the sentiments of its words.

    Args:
        word_sentiment (List[float]): The list of word sentiments.

    Returns:
        float: The calculated sentiment of the comment.

    """
    if len(word_sentiment) != 0:
        comment_sentiment = sum(word_sentiment) / len(word_sentiment)
    else:
        comment_sentiment = None
    return comment_sentiment

def display_sentiment(comment_sentiment: float, words_not_found: List[str]):
    """
    Displays the sentiment of a comment and any words that could not be measured.

    Arguments:
        comment_sentiment (float): The sentiment of the comment.
        words_not_found (List[str]): The list of words that could not be measured.

    """
    if comment_sentiment == None:
        print("")
        print("Unable to calculate sentiment! No data on queried comment.")
    elif comment_sentiment > 0:
        print("")
        print("This comment is positive")
        print("It's sentiment:", comment_sentiment)
    elif comment_sentiment == 0:
        print("")
        print("This comment is neutral")
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
    FILENAME_POSITIVE = "sample_data/positive/*"
    FILENAME_NEGATIVE = "sample_data/negative/*"
    # 1. Prompt the user to enter a comment
    user_text = get_user_text()
    # 2. Clean up the user's input
    cleaned_user_text = cleanup_user_input(user_text)
    # 3. Open positive and negative comments files
    positive_comments = open_files(FILENAME_POSITIVE)
    negative_comments = open_files(FILENAME_NEGATIVE)

    # 4. Count word occurrences in positive and negative comments
    all_words_sentiment = []
    words_not_found = []
    for word in cleaned_user_text:
        positive_count = count_word_occurrences(word, positive_comments)
        negative_count = count_word_occurrences(word, negative_comments)
        if positive_count == 0 and negative_count == 0:
            words_not_found.append(word)
        else:
            # 5. Calculate sentiment for each word
            word_sentiment = calculate_word_sentiment(positive_count, negative_count)
            all_words_sentiment.append(word_sentiment)
    
    comment_sentiment = calculate_comment_sentiment(all_words_sentiment)
    # 7. Display the sentiment to the user
    display_sentiment(comment_sentiment, words_not_found)

if __name__ == '__main__':
    main()
