import pytest
from movie_review_sentiment_analyzer import cleanup_user_input, calculate_word_sentiment, calculate_comment_sentiment

# Test cleanup_user_input function
def test_cleanup_user_input():
    text = "Hello!!! This is a test! <br />"
    cleaned_words = cleanup_user_input(text)
    assert cleaned_words == ["hello", "this", "is", "a", "test"]

# Test calculate_word_sentiment function
def test_calculate_word_sentiment():
    # Positive sentiment (more positive than negative occurrences)
    positive_count = 10
    negative_count = 5
    sentiment = calculate_word_sentiment(positive_count, negative_count)
    assert sentiment == 0.3333333333333333  

    # Negative sentiment (more negative than positive occurrences)
    positive_count = 5
    negative_count = 10
    sentiment = calculate_word_sentiment(positive_count, negative_count)
    assert sentiment == -0.3333333333333333  

    # Neutral sentiment (equal positive and negative occurrences)
    positive_count = 5
    negative_count = 5
    sentiment = calculate_word_sentiment(positive_count, negative_count)
    assert sentiment == 0.0

    # No sentiment (no positive or negative occurrences)
    positive_count = 0
    negative_count = 0
    sentiment = calculate_word_sentiment(positive_count, negative_count)
    assert sentiment == None

# Test calculate_comment_sentiment function
def test_calculate_comment_sentiment():
    # Test with positive word sentiments
    word_sentiments = [0.5, 0.7, 0.3]
    comment_sentiment = calculate_comment_sentiment(word_sentiments)
    assert comment_sentiment == pytest.approx(0.5)

    # Test with negative word sentiments
    word_sentiments = [-0.2, -0.5, -0.1]
    comment_sentiment = calculate_comment_sentiment(word_sentiments)
    assert comment_sentiment == pytest.approx(-0.26666666666666666)

    # Test with neutral word sentiments
    word_sentiments = [0.0, 0.0, 0.0]
    comment_sentiment = calculate_comment_sentiment(word_sentiments)
    assert comment_sentiment == pytest.approx(0.0)

    # Test with no data. No comment sentiment
    word_sentiments = []
    comment_sentiment = calculate_comment_sentiment(word_sentiments)
    assert comment_sentiment == None
    
