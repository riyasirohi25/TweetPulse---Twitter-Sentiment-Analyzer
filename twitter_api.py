import tweepy

# Replace with your keys
API_KEY = "1NsNTOE7lAcuylrLR9AIK47zz"
API_SECRET = "SivNuSf9Kcuk87rXsvBpWwh2upL3cNzjqqi6i6dajKGBbulo3V"
ACCESS_TOKEN = "1449734008225468416-H9nHQOGDEK3b8SvBBI9SFsEbw4LEVO"
ACCESS_SECRET = "UH2FQlPAJvYU00erzPUGEM0qbxEcrGlUSiW2qJktsXSgy"
BEARER_TOKEN = "AAAAAAAAAAAAAAAAAAAAAIg33wEAAAAAqskQ4PaSu%2FkVc7Hnoyu3QjHPpTI%3DaussyF4ZVVDPFWBIBVAuxpvekoiG7nJiJoUXkuoh4cXYjLUOiF"

# Use Client for v2 endpoints
client = tweepy.Client(bearer_token=BEARER_TOKEN,
                       consumer_key=API_KEY,
                       consumer_secret=API_SECRET,
                       access_token=ACCESS_TOKEN,
                       access_token_secret=ACCESS_SECRET)

# Search recent tweets
response = client.search_recent_tweets(query="Python", max_results=10)

for tweet in response.data:
    print(tweet.text)


