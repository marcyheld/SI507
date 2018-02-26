#analyze_tweets.py

import sqlite3
import nltk
import nltk.data
from nltk import word_tokenize,sent_tokenize

conn = sqlite3.connect('tweets.db')
cur = conn.cursor()

print('***** MOST FREQUENTLY MENTIONED AUTHORS *****')

# Print the 10 most frequently mentioned authors in the entire corpus
q = 'SELECT username, mentions_count FROM Authors ORDER BY mentions_count DESC'
r = cur.execute(q)
v = r.fetchall()

for row in v[:10]:
    print (row[0] + " is mentioned " + str(row[1]) + " times")

print('*' * 20, '\n\n') # dividing line for readable output



print('***** TWEETS MENTIONING AADL *****')

# Print all tweets that mention the twitter user 'aadl' (the Ann Arbor District Library)
q = 'SELECT [text], time_stamp '
q += 'FROM Tweets JOIN Mentions ON Tweets.tweet_id=Mentions.tweet_id '
q += 'WHERE Mentions.author_id = 13602482'
r = cur.execute(q)
v = r.fetchall()

for row in v:
    print (row[0] + ' (on ' + str(row[1]) + '+00:00)\n')

print('*' * 20, '\n\n')



print('***** MOST COMMON VERBS IN UMSI TWEETS *****')

# Print the 10 most common verbs ('VB' in the default NLTK part of speech tagger)
# that appear in tweets from the umsi account
q = 'SELECT [text] '
q += 'FROM Tweets '
q += 'WHERE author_id = 18033550'
r = cur.execute(q)
v = r.fetchall()

badList = ['@', '-', '_', b'\xe2\x80\xa6'.decode(), 'umsi', 'umsiasb17', 'umich', 'https']

verb_count = {}

for row in v:
    tokens = nltk.word_tokenize(row[0])
    tagged_tokens = nltk.pos_tag(tokens)
    for item in tagged_tokens:
        if item[1] == 'VB' and item[0] not in badList:
            #print(item)
            if item[0] not in verb_count:
                verb_count[item[0]] = 0
            verb_count[item[0]] += 1

#print (verb_count)
sorted_verbs = sorted(verb_count.keys(), key=lambda x: verb_count[x], reverse = True)
for word in sorted_verbs[:10]:
    print (word + " (" + str(verb_count[word]) + " times)")

print('*' * 20, '\n\n')



print('***** MOST COMMON VERBS IN UMSI "NEIGHBOR" TWEETS *****')

# Print the 10 most common verbs ('VB' in the default NLTK part of speech tagger)
# that appear in tweets from umsi's "neighbors", giving preference to tweets from
# umsi's most "mentioned" accounts
q = 'SELECT [text] '
q += 'FROM Tweets '
q += 'WHERE author_id != 18033550'
r = cur.execute(q)
v = r.fetchall()

badList = ['@', '-', '_', b'\xe2\x80\xa6'.decode(), 'umsi', 'umsiasb17', 'umich', 'https']

verb_count = {}

for row in v:
    tokens = nltk.word_tokenize(row[0])
    tagged_tokens = nltk.pos_tag(tokens)
    for item in tagged_tokens:
        if item[1] == 'VB' and item[0] not in badList:
            #print(item)
            if item[0] not in verb_count:
                verb_count[item[0]] = 0
            verb_count[item[0]] += 1

#print (verb_count)
sorted_verbs = sorted(verb_count.keys(), key=lambda x: verb_count[x], reverse = True)
for word in sorted_verbs[:10]:
    print (word + " (" + str(verb_count[word]) + " times)")

print('*' * 20, '\n\n')

conn.close()
