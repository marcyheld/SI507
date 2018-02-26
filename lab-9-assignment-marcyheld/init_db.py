import sqlite3

reset = True

conn = sqlite3.connect('tweets.db')
cur = conn.cursor()

if reset:
	cur.execute("DROP TABLE IF EXISTS Tweets")
	cur.execute("DROP TABLE IF EXISTS Hashtags")


# Create a table to store Tweets
statement = 'CREATE TABLE IF NOT EXISTS '
statement += 'Tweets (tweet_id INTEGER primary key, tweet_text TEXT, likes INTEGER)'
cur.execute(statement)
# Create a table to store Hashtags
statement2 = 'CREATE TABLE IF NOT EXISTS '
statement2 += 'Hashtags (hashtag_id INTEGER primary key autoincrement, hashtag_text TEXT, num_occurrences INTEGER)'
cur.execute(statement2)
# INSERT INTO (None, val1, val2)
# INSERT INTO Hashtags (hashtag_text, num_occurrences) VALUES (?,?)** this way is better!!!!!!
# cur.execute(statement2, NAME OF TUPLE WITH 2 VALUES GOES HERE !!)

# INSERT INTO Hashtags (hashtag_text, num_occurrences) VALUES (?,?)** this way is better!!!!!!


# Do you need a third table? YES!!
statement3 = 'CREATE TABLE IF NOT EXISTS '
statement3 += 'Mapping (tweet_id INTEGER, hashtag_id INTEGER, FOREIGN KEY (tweet_id) REFERENCES Tweets(tweet_id), FOREIGN KEY(hashtag_id) REFERENCES Hashtags(hashtag_id))'
cur.execute(statement3)

conn.commit()
