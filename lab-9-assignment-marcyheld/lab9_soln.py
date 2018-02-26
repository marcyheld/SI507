import tweepy
from tweepy import OAuthHandler
import json
import sqlite3

# from lab9_config import CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET
CONSUMER_KEY = ""
CONSUMER_SECRET = ""
ACCESS_TOKEN = "-"
ACCESS_TOKEN_SECRET = ""

def fetch_tweets(api):
	with open('tweets.json', 'w') as json_file:
		page = 1
		num_tweets = 0
		while True:
			tweets = api.user_timeline('taylorswift13', page=page)
			if tweets:
				for tweet in tweets:
					if num_tweets >= 300:
						break

					json_tweet = tweet._json # convert to JSON format
					json_file.write(json.dumps(json_tweet))
					json_file.write('\n')
					num_tweets += 1
			else:
				break
			page += 1

			if num_tweets >= 300:
				break

		print ('Wrote', num_tweets, 'tweets to file.')

# Another valid solution
def fetch_tweets2(api):
	with open('tweets2.json', 'w') as json_file:
		for tweet in tweepy.Cursor(api.user_timeline, id='taylorswift13').items(300):
			json_file.write(json.dumps(tweet._json))
			json_file.write('\n')


def init_db():
	reset = True
	conn = sqlite3.connect('tweets.db')
	cur = conn.cursor()

	if reset:
		cur.execute("DROP TABLE IF EXISTS Tweets")
		cur.execute("DROP TABLE IF EXISTS Hashtags")
		cur.execute("DROP TABLE IF EXISTS HashtagTweetMap")

	statement = 'CREATE TABLE IF NOT EXISTS '
	statement += 'Tweets (tweet_id INTEGER PRIMARY KEY, tweet_text TEXT, likes INTEGER)'
	cur.execute(statement)

	statement = 'CREATE TABLE IF NOT EXISTS '
	statement += 'Hashtags (hashtag_id INTEGER PRIMARY KEY AUTOINCREMENT, hashtag_text TEXT, num_occurrences INTEGER)'
	cur.execute(statement)

	statement = 'CREATE TABLE IF NOT EXISTS '
	statement += 'HashtagTweetMap (hashtag_id INTEGER, tweet_id INTEGER)'
	cur.execute(statement)

	conn.close()


def save_hashtag(hashtag_text, cur, conn):
	select_sql = 'SELECT * FROM Hashtags WHERE hashtag_text = ?'
	cur.execute(select_sql, (hashtag_text,))
	if not cur.fetchone():
		insert_sql = 'INSERT INTO Hashtags (hashtag_text, num_occurrences) VALUES (?, ?)'
		cur.execute(insert_sql, (hashtag_text, 0))
		conn.commit()

	hashtag_id = None
	select_sql = 'SELECT hashtag_id FROM Hashtags WHERE hashtag_text = ?'
	cur.execute(select_sql, (hashtag_text,))
	hashtag_id = cur.fetchone()[0]

	return hashtag_id

def update_hashtag(tweet_id, hashtag, cur, conn):
	hashtag_text = hashtag['text']

	hashtag_id = save_hashtag(hashtag_text, cur, conn)

	update_sql = 'UPDATE Hashtags SET num_occurrences = num_occurrences + 1 WHERE hashtag_text = ?'
	cur.execute(update_sql, (hashtag_text,))
	conn.commit()

	map_sql = 'SELECT * FROM HashtagTweetMap WHERE hashtag_id = ? AND tweet_id = ?'
	cur.execute(map_sql, (hashtag_id, tweet_id))
	if not cur.fetchone():
		insert_sql = 'INSERT INTO HashtagTweetMap VALUES (?, ?)'
		cur.execute(insert_sql, (hashtag_id, tweet_id))
		conn.commit()


def save_tweet(json_tweet, cur, conn):
	tweet_id = json_tweet['id']
	text = json_tweet['text']
	likes = json_tweet['favorite_count']

	select_sql = 'SELECT * FROM Tweets WHERE tweet_id=' + str(tweet_id)
	cur.execute(select_sql)
	if not cur.fetchone():
		insert_sql = 'INSERT INTO Tweets VALUES (?, ?, ?)'
		cur.execute(insert_sql, (tweet_id, text, likes))
		conn.commit()

	hashtags = json_tweet['entities']['hashtags']
	for hashtag in hashtags:
		update_hashtag(tweet_id, hashtag, cur, conn)

def add_to_db():
	conn = sqlite3.connect('tweets.db')
	cur = conn.cursor()

	with open('tweets.json', 'r') as json_file:
		for line in json_file:
			line = line.lstrip().rstrip()
			if len(line) == 0:
				continue

			json_tweet = json.loads(line)
			save_tweet(json_tweet, cur, conn)

	conn.close()


def most_common_hashtags(cur, conn):
	select_sql = 'SELECT hashtag_text FROM Hashtags ORDER BY num_occurrences DESC'
	cur.execute(select_sql)

	print ('Most common hashtags:')
	for row in cur.fetchmany(size=20):
		print (row[0])

def fifty_shades_darker(cur, conn):
	select_sql = 'SELECT hashtag_id FROM Hashtags WHERE hashtag_text = ?'
	cur.execute(select_sql, ('fiftyshadesdarker',))
	hashtag_id = cur.fetchone()[0]

	select_sql = 'SELECT Tweets.tweet_id, Tweets.tweet_text FROM Tweets JOIN HashtagTweetMap ON HashtagTweetMap.tweet_id = Tweets.tweet_id WHERE HashtagTweetMap.hashtag_id = ?'
	cur.execute(select_sql, (hashtag_id,))

	print ('Tweets containing #fiftyshadesdarker')
	for row in cur.fetchall():
		print ('\t'.join([repr(item) for item in row]))


def query_db():
	conn = sqlite3.connect('tweets.db')
	cur = conn.cursor()

	most_common_hashtags(cur, conn)
	fifty_shades_darker(cur, conn)

	conn.close()

# Authorization setup to access the Twitter API
auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)

fetch_tweets(api)
init_db()
add_to_db()
query_db()
