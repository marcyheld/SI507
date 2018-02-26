import tweepy
from tweepy import OAuthHandler
import datetime
import json
import sqlite3

conn = sqlite3.connect('tweets.db')
cur = conn.cursor()

from proj3_config import CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET

auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)

with open('proj3_tweets.json', 'w') as json_file:
    page = 1
    while page <= 25:
        print (str(page))
        #sinceID = 771003081756700673
        tweets = api.user_timeline(id='umsi', page=page)
        if tweets:
            for tweet in tweets:
                if tweet.created_at > datetime.datetime(2016,9,1):
                    statement = 'INSERT INTO Tweets VALUES (?, ?, ?, ?)'
                    data = (tweet.id, tweet.user.id, tweet.text, tweet.created_at)
                    cur.execute(statement, data)
                    #print (tweet.created_at)

                    json_tweet = tweet._json # convert to JSON format
                    json.dump(json_tweet, json_file)
                    json_file.write('\n')
        else:
            break

        page += 1

conn.commit()
conn.close()
