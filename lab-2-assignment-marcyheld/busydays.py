# NOTE: mbox-short.txt, mbox.txt, test1.txt, test2.txt deleted for security purposes

fname = input('Please enter a file name to test: ')

try:
	fileobj = open(fname, 'r')
	filelines = fileobj.readlines()

	dayCount = {}
	for aline in filelines:
		if aline.startswith("X-DSPAM-Processed"):
			if aline[19:22] not in dayCount:
				dayCount[aline[19:22]] = 0
			dayCount[aline[19:22]] += 1

	fileobj.close()

	dayValues = dayCount.items()

	sortedDayCount = sorted(dayValues, key = lambda x:x[1], reverse = True)

	for item in sortedDayCount:
	 	print (str(item[1]) + " " + str(item[0]))

except:
	print ('Invalid file name!')
