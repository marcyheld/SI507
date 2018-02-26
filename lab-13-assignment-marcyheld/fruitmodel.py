
data = [
		("apples", 6), 
		("bananas", 7), 
		("grapes", 4),
		("pineapple", 1),
		("cherries", 15)
		]

def get_data():
	return data

def get_sorted_data():
	return sorted(data, key=lambda x : x[1], reverse=True)