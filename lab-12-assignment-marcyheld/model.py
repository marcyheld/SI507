def get_data(csv_file):
	# Open CSV file and return a list of tuples.
	fileInput = open(csv_file, "r")
	returnList = []

	for row in fileInput:
		getRidOfNewline = row.strip()
		rowItems = getRidOfNewline.split(',')
		listItem = (rowItems[0], rowItems[1], rowItems[2])
		#print (listItem)
		returnList.append(listItem)

	fileInput.close()

	return returnList

print(get_data("data.csv"))
