#db_test.py

import sqlite3

conn = sqlite3.connect("tweets.db")
cur = conn.cursor()

points = 0

# Task 1

# at least 300 tweets?
try:
	q = 'SELECT COUNT(*) FROM Tweets WHERE author_id=18033550' # umsi account id
	r = cur.execute(q)
	v = r.fetchone()[0]

	if v > 300:
		points += 5
except:
	pass

# no tweets before Sept 1, 2016?
try:
	q = 'SELECT COUNT(*) FROM Tweets WHERE time_stamp > "2016-09-01 00:00"'
	r = cur.execute(q)
	v = r.fetchone()[0]

	q = 'SELECT COUNT(*) FROM Tweets WHERE time_stamp <= "2016-09-01 00:00"'
	r = cur.execute(q)
	v2 = r.fetchone()[0]

	if v > 0 and v2 == 0:
		points += 5
except:
	pass

# contains exactly one copy of an arbitrary tweet from Nov 30
try:
	q = 'SELECT COUNT(*) FROM Tweets WHERE tweet_id=804011935658287105'
	r = cur.execute(q)
	v = r.fetchone()[0]

	if v == 1:
		points += 5
except:
	pass

print('Task 1 points:', points)


# Task 2

points = 0

# can link from a tweet to its author
try:
	q = 'SELECT username FROM Authors JOIN Tweets '
	q += 'ON Tweets.author_id=Authors.author_id WHERE tweet_id=827203934905364480'
	r = cur.execute(q)
	v = r.fetchone()[0]

	if v == 'umsi':
		points += 5
except:
	pass

# can look up a mentioned authors for a tweet
try:
	q = 'SELECT COUNT(*) FROM Authors '
	q += 'JOIN Mentions ON Authors.author_id = Mentions.author_id '
	q += 'JOIN Tweets ON Mentions.tweet_id = Tweets.tweet_id '
	q += 'WHERE Tweets.tweet_id = 805816623810703360' # aadl
	r = cur.execute(q)
	v = r.fetchone()[0]

	if v == 4:
		points += 5
except:
	pass

# verify no duplicate authors
try:
	q = 'SELECT COUNT(*) FROM Authors'
	r = cur.execute(q)
	v = r.fetchone()[0]

	q = 'SELECT COUNT(DISTINCT author_id) FROM Authors'
	r = cur.execute(q)
	v2 = r.fetchone()[0]

	if v == v2:
		points += 5
except:
	pass
print('Task 2 points:', points)

conn.close()
