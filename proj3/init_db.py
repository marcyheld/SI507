#init_db.py

import sqlite3
import json
import datetime

reset = True

conn = sqlite3.connect('tweets.db')
cur = conn.cursor()

if reset:
    cur.execute("DROP TABLE IF EXISTS Tweets")
    cur.execute("DROP TABLE IF EXISTS Authors")
    cur.execute("DROP TABLE IF EXISTS Mentions")

# Put code here to create the database and tables
#
# You may want to set this up so that you can also DROP or TRUNCATE tables
# as you are developing so that you can start from scratch when you need to

statement = 'CREATE TABLE IF NOT EXISTS '
statement += 'Tweets (tweet_id INTEGER PRIMARY KEY, author_id INTEGER, text TEXT, time_stamp TEXT)'
cur.execute(statement)

statement2 = 'CREATE TABLE IF NOT EXISTS '
statement2 += 'Authors (author_id INTEGER PRIMARY KEY, username TEXT, mentions_count INTEGER)'
cur.execute(statement2)

statement3 = 'CREATE TABLE IF NOT EXISTS '
statement3 += 'Mentions (tweet_id INTEGER, author_id INTEGER)'
cur.execute(statement3)

# statement3 = 'CREATE TABLE IF NOT EXISTS'
# statement3 += 'Mentions ()'

# with open('proj3_tweets.json', 'r') as inputFile:
#     for line in inputFile:
#         tweet = json.loads(line)
#         #print (type(tweet['created_at']))
#
#         statement = 'INSERT INTO Tweets VALUES (?, ?, ?, ?)'
#         data = (tweet['id'], tweet['user']['id'], tweet['text'], tweet['created_at'])
#         cur.execute(statement, data)

# tweet[created_at] IS NOT THE SAME AS tweet.created_at
# THE PYTHON DICTIONARY OBJECT (which is a dictionary version of a tweet object)
# DOES NOT HAVE THE METHOD .created_at

# ALSO, how to go to other twitter users' pages and find WHERE tweets Starting
# on Sept 1, 2016 begin?? How to make the tweepy API

conn.commit()
conn.close()
