import os
import csv

import tweepy
from textblob import TextBlob

# Step 1 - Authenticate
consumer_key=os.environ['CONSUMER_KEY']
consumer_secret=os.environ['CONSUMER_SECRET']

access_token=os.environ['ACCESS_TOKEN']
access_token_secret=os.environ['ACCESS_TOKEN_SECRET']

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

#Step 3 - Retrieve Tweets
public_tweets = api.search('Trump')



#CHALLENGE - Instead of printing out each tweet, save each Tweet to a CSV file
#and label each one as either 'positive' or 'negative', depending on the sentiment
#You can decide the sentiment polarity threshold yourself


with open('data.csv', 'w') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=',',
                            quotechar='"', quoting=csv.QUOTE_MINIMAL)
    spamwriter.writerow(['label', 'tweet'])
    for tweet in public_tweets:
        text = tweet.text
        #Step 4 Perform Sentiment Analysis on Tweets
        analysis = TextBlob(text)
        label = 'neutral'
        if analysis.sentiment.polarity < 0:
            label = 'negative'
        if analysis.sentiment.polarity > 0:
            label = 'positive'
        spamwriter.writerow([label, text.replace('\n', '\\n')])
