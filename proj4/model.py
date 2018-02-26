
import csv

data_is_loaded = False

def load_data():

	with open('US_County_Level_Presidential_Results_12-16.csv', 'r') as csvfile:
	    reader = csv.reader(csvfile, delimiter=',')
	    returnList = []

	    for row in reader:
	    	if row[9] != "AK":
	    		returnList.append(row)

	    data_is_loaded = True
	    return returnList

def get_data(party='dem', raw=True, sort_ascending=True, year=2016):
	if not data_is_loaded:
		info = load_data()

	rawVotesCount = {}
	totalVotesCount = {}
	voteCountTuples = []

	# accumulate TOTAL votes for each state (add each county total together)
	# we will use this total later if raw = False in get_data params
	for row in info[1:]:
		if row[9] not in totalVotesCount:
			totalVotesCount[row[9]] = 0
		totalVotesCount[row[9]] += float(row[4])

	# if 'dem' selected, accumulate all raw 'dem' votes for each state
	if party == 'dem':
		for row in info[1:]:
			if row[9] not in rawVotesCount:
				rawVotesCount[row[9]] = 0 #{}
			rawVotesCount[row[9]] += float(row[2])

	# if 'gop' selected, accumulate all raw 'gop' votes for each state
	elif party == 'gop':
		for row in info[1:]:
			if row[9] not in rawVotesCount:
				rawVotesCount[row[9]] = 0
			rawVotesCount[row[9]] += float(row[3])

	# if raw = True, create list of tuples with (state, rawVoteCount)
	if raw == True:
		for state in rawVotesCount.keys():
			voteCountTuples.append((state, rawVotesCount[state]))

	# if raw = False, create list of tuples with (state, votePercentage)
	elif raw == False: 
		for state in rawVotesCount.keys():
			voteCountTuples.append((state, (rawVotesCount[state] / totalVotesCount[state])))

	# if sort_ascending = True, sort list of tuples from lowest to highest
	if sort_ascending == True:
	 	sorted_votes = sorted(voteCountTuples, key = lambda x:x[1])

	# if sort_ascending = False, sort list of tuples from highest to lowest
	elif sort_ascending == False:
	 	sorted_votes = sorted(voteCountTuples, key = lambda x:x[1], reverse=True)

	# return tuple of (state abbrev, raw vote tally OR percentage)
	return (sorted_votes)

if __name__ == "__main__":

	points = 0

	data = get_data()
	if data[0] == ('WY', 55949.0) and data[-1] == ('CA', 7362490.0):
		points += 3.33

	data = get_data(party='gop', raw=False)
	if data [0][0] == 'DC' and int(data[0][1] * 100) == 4 and \
		data[-1][0] == 'WY' and int(data[-1][1] * 100) == 70:
		points += 3.33

	data = get_data(party='dem', raw=True, sort_ascending=False)
	if data[0] == ('CA', 7362490.0) and data[-1] == ('WY', 55949.0):
		points += 3.34

	print("points :", points)
