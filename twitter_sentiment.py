# twitter_sentiment.py

import tweepy
import re
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
import matplotlib.pyplot as plt

# Make sure NLTK can find vader_lexicon
nltk.data.path.append(r'C:\Users\Lenovo\AppData\Roaming\nltk_data')
nltk.download('vader_lexicon')

# Initialize VADER
sia = SentimentIntensityAnalyzer()

# -----------------------------
# Replace these with your Twitter API keys
API_KEY = "1NsNTOE7lAcuylrLR9AIK47zz"
API_SECRET = "SivNuSf9Kcuk87rXsvBpWwh2upL3cNzjqqi6i6dajKGBbulo3V"
ACCESS_TOKEN = "1449734008225468416-H9nHQOGDEK3b8SvBBI9SFsEbw4LEVO"
ACCESS_SECRET = "UH2FQlPAJvYU00erzPUGEM0qbxEcrGlUSiW2qJktsXSgy"
BEARER_TOKEN = "AAAAAAAAAAAAAAAAAAAAAIg33wEAAAAAqskQ4PaSu%2FkVc7Hnoyu3QjHPpTI%3DaussyF4ZVVDPFWBIBVAuxpvekoiG7nJiJoUXkuoh4cXYjLUOiF"
# -----------------------------

# Connect to Twitter API v2 (just need Bearer Token for recent tweets)
client = tweepy.Client(bearer_token=BEARER_TOKEN)

# Function to clean tweet text
def clean_tweet(tweet):
    tweet = re.sub(r'@[\w]+', '', tweet)    # Remove mentions
    tweet = re.sub(r'http\S+', '', tweet)   # Remove URLs
    tweet = re.sub(r'#', '', tweet)         # Remove hashtag symbols
    tweet = re.sub(r'[^A-Za-z\s]+', '', tweet)  # Remove special chars
    tweet = tweet.lower()                    # Lowercase
    return tweet

# Fetch recent tweets
query = "Python"   # Change this keyword if you want
max_tweets = 20    # Between 10-100 for Twitter v2 API
response = client.search_recent_tweets(query=query, max_results=max_tweets)

# Dictionary to store sentiment counts
sentiments_count = {'Positive': 0, 'Neutral': 0, 'Negative': 0}

print(f"\nSentiment Analysis for recent tweets about '{query}':\n")
for tweet in response.data:
    cleaned = clean_tweet(tweet.text)
    score = sia.polarity_scores(cleaned)
    
    if score['compound'] > 0.05:
        sentiment = 'Positive'
    elif score['compound'] < -0.05:
        sentiment = 'Negative'
    else:
        sentiment = 'Neutral'
    
    sentiments_count[sentiment] += 1
    
    print(f"Tweet: {cleaned}")
    print(f"Sentiment: {sentiment} | Score: {score}\n")

# Plot sentiment counts
plt.bar(sentiments_count.keys(), sentiments_count.values(), color=['green', 'gray', 'red'])
plt.title(f"Sentiment Analysis of '{query}' Tweets")
plt.ylabel("Number of Tweets")
plt.show()
