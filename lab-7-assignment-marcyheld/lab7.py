# code developed by Jackie Cohen; revised by Paul Resnick
# further revised by Colleen van Lent for Python3
# further revised by Karthik Ramanathan and Megh Marathe
import nltk
import nltk.data
import random
from nltk import word_tokenize,sent_tokenize

def main():
	text_data = ""
	tagmap = {"NN":"a noun","NNS":"a plural noun", "NNP": "a proper noun", "NNPS": "a plural proper noun",
				"JJ":"an adjective", "JJR":"a comparative adjective (ex: 'larger')", "JJS":"a superlative adjective (ex: 'largest')"}
	final_words = []

	# TODO 1: Read the text file "gutenberg.txt" and store it in the variable text_data
	# Write your code here
	textFileObj = open("gutenberg.txt")
	gut_words_str = textFileObj.read()
	#gut_words_lst = gut_words_str.split()

	#print (gut_words_lst)
	tokens = nltk.word_tokenize(gut_words_str) # strings split up into words
	#print (tokens)
	tagged_tokens = nltk.pos_tag(tokens) # words get tagged
	print(tagged_tokens)

	nouns = []
	adj = []

	for item in tagged_tokens:
		if item[1] == "NN" or item[1] == "NNS" or item[1] == "NNP" or item[1] == "NNPS":
			nouns.append(item)
		elif item[1] == "JJ" or item[1] == "JJR" or item[1] == "JJS":
			adj.append(item)

	#print ("Nouns: " + str(nouns))
	#print ("Adjectives: " + str(adj))

	sel_nouns = []
	noun_rand1 = random.randrange(len(nouns))
	noun1Type = nouns[noun_rand1][1]
	print (noun1Type)
	sel_nouns.append(nouns[noun_rand1][0])

	noun_rand2 = random.randrange(len(nouns))
	noun2Type = nouns[noun_rand2][1]
	print (noun2Type)
	sel_nouns.append(nouns[noun_rand2][0])

	sel_adjs = []
	adj_rand1 = random.randrange(len(adj))
	adj1Type = adj[adj_rand1][1]
	print(adj1Type)
	sel_adjs.append(adj[adj_rand1][0])

	adj_rand2 = random.randrange(len(adj))
	adj2Type = adj[adj_rand2][1]
	print(adj2Type)
	sel_adjs.append(adj[adj_rand2][0])

	print ("Selected Nouns: " + str(sel_nouns))
	print ("Selected Adjectives: " + str(sel_adjs))



	for (word, tag) in tagged_tokens:
		if word not in sel_nouns and word not in sel_adjs:
			final_words.append(word)
		else:
			# TODO 4: If the word is among the randomly selected nouns or adjectives, prompt the user
			# to add a new word and append the new word to the list of final_words.
			# Write your code here
			userAdj1 = input("Please enter " + tagmap[adj1Type] + ":\n")
			userNoun1 = input("Please enter " + tagmap[noun1Type] + ":\n")
			userAdj2 = input("Please enter " + tagmap[adj2Type] + ":\n")
			userNoun2 = input("Please enter " + tagmap[noun1Type] + ":\n")

			final_words.append()


	# Code for printing the old version of the text
	print("******* OLD TEXT *******")
	print(" ".join(tokens))

	print("\n\n******* NEW TEXT *******")
	# TODO 5: Print the new text
	# Write your code here
	textFileObj.close()

main()
