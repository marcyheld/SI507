import sqlite3
import json

conn = sqlite3.connect('tweets.db')
cur = conn.cursor()

tweetID_mentions = {}
mentionsLst = []

with open('proj3_tweets.json', 'r') as inputFile:
    for tweet in inputFile:
        json_tweet = json.loads(tweet)
        if json_tweet['entities']['user_mentions']:
            for i in json_tweet['entities']['user_mentions']:
                mentionsLst.append(i['id'])
            tweetID_mentions[json_tweet['id']] = mentionsLst
            mentionsLst = []

inputFile.close()

with open('proj3_mentiontweets.json', 'r') as inputFile:
    for tweet in inputFile:
        json_tweet = json.loads(tweet)
        if json_tweet['entities']['user_mentions']:
            for i in json_tweet['entities']['user_mentions']:
                mentionsLst.append(i['id'])
            tweetID_mentions[json_tweet['id']] = mentionsLst
            mentionsLst = []


#print (tweetID_mentions)
# print (tweetID_mentions[845034493064957953])
# print (tweetID_mentions[844951880425967617])

for item in tweetID_mentions.keys():
    num = 0
    for mention in tweetID_mentions[item]:
        statement = 'INSERT INTO Mentions VALUES (?, ?)'
        data = (item, tweetID_mentions[item][num])
        cur.execute(statement, data)

        num += 1


conn.commit()
conn.close()
