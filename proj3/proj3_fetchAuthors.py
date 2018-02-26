import json
import sqlite3
import tweepy
from tweepy import OAuthHandler
import datetime

conn = sqlite3.connect('tweets.db')
cur = conn.cursor()

unique_authors = {}
author_mention_count = {}

with open('proj3_tweets.json', 'r') as inputFile:
    for tweet in inputFile:
        json_tweet = json.loads(tweet)
        if json_tweet['entities']['user_mentions']:
            for i in json_tweet['entities']['user_mentions']:
                if i['id'] not in unique_authors:
                    author_mention_count[i['id']] = 0
                    unique_authors[i['id']] = i['screen_name']
                author_mention_count[i['id']] += 1

# insert into tweets.db
# item is each key in unique_authors.keys(), which is the id number
# unique_authors[item] is the screen name that matches that id
# author_mention_count[item] is the mention count for that id
# (the author id number is the key in both unique_authors and
# author_mention_count dictionaries!!!!!!)

# ******** UNCOMMENT THE FOLLOWING LINES BEFORE TURNING IN !!! ********
# for item in unique_authors.keys():
#     statement = 'INSERT INTO Authors VALUES (?, ?, ?)'
#     data = (item, unique_authors[item], author_mention_count[item])
#     cur.execute(statement, data)

# print (unique_authors[18033550])
#print (author_mention_count)
#print (len(unique_authors.keys()))

# Have sorted author mentions, exclude the first one, add these tweets to
# Tweets database !!!!!!!!!!!!!!!!!!!!!!!!!!
sorted_mentions = sorted(author_mention_count.keys(), key=lambda x: author_mention_count[x], reverse = True)

from proj3_config import CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET

auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)

with open('proj3_mentiontweets.json', 'w') as json_file:
    tweet_count = 0

    for user_id in sorted_mentions[1:]:
        tweets = api.user_timeline(id=user_id, page=1)
        if tweets:
            for tweet in tweets:
                if tweet.created_at > datetime.datetime(2016,9,1) and tweet_count < 400:
                    print (str(tweet_count))
                    statement = 'INSERT INTO Tweets VALUES (?, ?, ?, ?)'
                    data = (tweet.id, tweet.user.id, tweet.text, tweet.created_at)
                    cur.execute(statement, data)

                    json_tweet = tweet._json # convert to JSON format
                    json.dump(json_tweet, json_file)
                    json_file.write('\n')
                    tweet_count += 1
        else:
            break

json_file.close()

    #print (item, ':', author_mention_count[item])
#print (sorted_mentions)

with open('proj3_mentiontweets.json', 'r') as inputFile:
    for tweet in inputFile:
        json_tweet = json.loads(tweet)
        if json_tweet['entities']['user_mentions']:
            for i in json_tweet['entities']['user_mentions']:
                if i['id'] not in unique_authors:
                    author_mention_count[i['id']] = 0
                    unique_authors[i['id']] = i['screen_name']
                author_mention_count[i['id']] += 1

for item in unique_authors.keys():
    statement = 'INSERT INTO Authors VALUES (?, ?, ?)'
    data = (item, unique_authors[item], author_mention_count[item])
    cur.execute(statement, data)

conn.commit()
conn.close()
