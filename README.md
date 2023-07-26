# Sentiment Analysis of Movie Reviews

This script is designed to perform Sentiment Analysis of movie reviews. It analyzes a dataset comprising 50,000 movie reviews, allowing automatic determination of the sentiment (positive, negative, or neutral) of new comments and online statements. The main objective is to identify the most positive and negative expressions among millions of neutral comments, enabling users to highlight positive comments and address negative ones before they reach a wider audience. This tool aids in efficiently gauging audience sentiment towards movies and can be valuable for making data-driven decisions in the film industry.

## Table of Contents
* [General Info](#general-info)
* [Features](#features)
* [Technologies Used](#technologies-used)
* [Prerequisites](#prerequisites)
* [Setup](#setup)
* [Testing for Development](#testing-for-velopment)
* [Solutions](#solutions)
* [Tools and Plugins](#tools-and-plugins)
* [Future Plans](#future-plans)
* [Inspirations and Acknowledgments](#inspirations-and-acknowledgments)

## General Info
This script performs Sentiment Analysis on user-entered comments by analyzing word sentiments in a dataset of positive and negative movie reviews.

## Features
* Prompt the user to write a comment for sentiment analysis.
* Clean up the user's input by removing punctuation and converting it to lowercase.
* Open and read positive and negative movie review files from 'positive.txt' and 'negative.txt' in the 'sample_data' folder.
* Count occurrences of words in positive and negative movie reviews.
* Calculate sentiment for each word based on positive and negative occurrences.
* Calculate sentiment for the entire comment based on the sentiments of its words.
* Display the sentiment of the comment and any words that could not be measured.

## Technologies Used
* Python

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

## Prerequisites
Before running the script, ensure you have the following:
* Python 3.11.2 installed on your system.
* Sample data files 'positive.txt' and 'negative.txt' containing positive and negative movie reviews.

## Setup
To run the project locally, follow these steps:

- Clone this repository to your local machine.
- Navigate to the project directory.
- Run the program:
```
python3 movie_review_sentiment_analyzer.py.py
```

## Testing for Development
To ensure the correctness of the `movie_review_sentiment_analyzer.py` module, we have created a test suite in `test_movie_review_sentiment_analyzer.py` using pytest.

These tests will help ensure that the sentiment analysis functions, such as `cleanup_user_input`, `calculate_word_sentiment`, and `calculate_comment_sentiment`, are working as expected. The test cases cover various scenarios, including positive, negative, and neutral sentiments, as well as cases where some words cannot be measured.

### Running Tests
To run the tests, follow these steps:

1. Install pytest if you haven't already, by:
``` 
pip3 install pytest
```
2. Navigate to the project directory.

3. Run the tests:
```
pytest test_movie_review_sentiment_analyzer.py
```

## Solutions
The script provides a solution for analyzing sentiments of movie reviews, allowing for quick identification of positive and negative expressions.

## Tools and Plugins
The script utilizes the following Python libraries:
* glob
* string
* typing

## Future Plans
Currently, the script focuses on analyzing movie review sentiments. In the future, I may extend its functionality to analyze sentiments in different domains, such as product reviews or social media comments.

## Inspirations and Acknowledgments
The program was adapted during the "Practical Python" training course. Thanks for the inspiring material and support!
