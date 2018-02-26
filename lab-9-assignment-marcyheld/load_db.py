import json
import sqlite3

conn = sqlite3.connect('tweets.db')
cur = conn.cursor()

with open('tweets.json', 'r') as json_file:
	for line in json_file:
		tweet_info = json.loads(line)
		print (type(line))
