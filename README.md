# TweetPulse: Twitter Sentiment Analyzer

A **Streamlit web app** that fetches tweets for any topic and determines the **overall sentiment** using **VADER sentiment analysis**. The app visualizes the sentiment distribution in a **pie chart**, making it easy to understand the general mood of Twitter users about a topic.  

---

## Features
- Fetches recent tweets using **Twitter API v2** with Bearer Token  
- Analyzes sentiment: **Positive, Neutral, Negative**  
- Displays the **overall sentiment** for a topic  
- Shows a **pie chart** for sentiment distribution  
- Simple, interactive interface via **Streamlit**  

---

## Tech Stack
- Python  
- Streamlit  
- NLTK (VADER Sentiment Analyzer)  
- Requests  
- Pandas  
- Matplotlib
- Tweepy (Twitter API V2)  

---

## Commands
1. Clone the repository:  
   `git clone https://github.com/YOUR_USERNAME/YOUR_REPO.git`  
   `cd YOUR_REPO`

2. Open `app.py` and replace `YOUR_BEARER_TOKEN` with your actual token.  
   Example: `BEARER_TOKEN = "YOUR_ACTUAL_TOKEN"`  
   **Important:** Keep this token secret, do NOT push it to GitHub.

3. Run the app:  
   `streamlit run app.py`

---

## Usage & Screenshots

### 1️⃣ Normal Interface
<img width="1916" height="1137" alt="image" src="https://github.com/user-attachments/assets/6b0cde1d-a603-4141-af84-ec34eff76d85" />


### 2️⃣ After Adding Topic
<img width="1916" height="1139" alt="image" src="https://github.com/user-attachments/assets/02fdfedd-675a-4a5b-83d6-99d9e2be8d28" />


### 3️⃣ Result with Sentiment Pie Chart
<img width="1918" height="1143" alt="image" src="https://github.com/user-attachments/assets/ebcd77e6-1806-4183-b861-907c607d9b3c" />


- Enter a topic or hashtag in the input field.  
- Choose the number of tweets to analyze (up to 100).  
- Click **Analyze Sentiment**.  
- See the **overall sentiment** and **pie chart** of Positive, Neutral, and Negative tweets.  

---

