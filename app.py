import streamlit as st
import requests
import pandas as pd
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import matplotlib.pyplot as plt

# 1️⃣ Twitter Bearer Token
BEARER_TOKEN = "AAAAAAAAAAAAAAAAAAAAAIg33wEAAAAAqskQ4PaSu%2FkVc7Hnoyu3QjHPpTI%3DaussyF4ZVVDPFWBIBVAuxpvekoiG7nJiJoUXkuoh4cXYjLUOiF"

# 2️⃣ Function to get tweets using Twitter API v2
def get_tweets(topic, max_results=100):
    url = "https://api.twitter.com/2/tweets/search/recent"
    headers = {"Authorization": f"Bearer {BEARER_TOKEN}"}
    params = {
        "query": topic + " -is:retweet lang:en",
        "max_results": min(max_results, 100),  # max 100 per request
        "tweet.fields": "text"
    }
    response = requests.get(url, headers=headers, params=params)
    if response.status_code != 200:
        st.error(f"Error fetching tweets: {response.status_code}")
        return []
    tweets = response.json().get("data", [])
    return [tweet["text"] for tweet in tweets]

# 3️⃣ Streamlit UI
st.title("TweetPulse: Twitter Sentiment Analyzer")
topic = st.text_input("Enter a topic or hashtag", "#")
num_tweets = st.slider("Number of tweets to analyze (max 100)", 10, 100, 50)

if st.button("Analyze Sentiment"):
    tweet_texts = get_tweets(topic, num_tweets)
    
    if not tweet_texts:
        st.warning("No tweets found for this topic.")
    else:
        # 4️⃣ Sentiment Analysis
        sid = SentimentIntensityAnalyzer()
        sentiments = {"Positive": 0, "Neutral": 0, "Negative": 0}

        for text in tweet_texts:
            score = sid.polarity_scores(text)
            if score['compound'] > 0.05:
                sentiments["Positive"] += 1
            elif score['compound'] < -0.05:
                sentiments["Negative"] += 1
            else:
                sentiments["Neutral"] += 1

        # 5️⃣ Determine overall sentiment
        overall = max(sentiments, key=sentiments.get)
        st.subheader(f"Overall Sentiment for '{topic}': {overall}")

        # 6️⃣ Convert to DataFrame for plotting
        df = pd.DataFrame(list(sentiments.items()), columns=['Sentiment', 'Count'])

        # 7️⃣ Display pie chart
        fig, ax = plt.subplots()
        ax.pie(df['Count'], labels=df['Sentiment'], autopct='%1.1f%%', colors=['#2ecc71', '#95a5a6', '#e74c3c'])
        ax.set_title("Sentiment Distribution")
        st.pyplot(fig)
