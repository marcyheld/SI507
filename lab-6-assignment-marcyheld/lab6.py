import urllib.parse
import urllib.request
import json
import ssl

base_url = 'https://maps.googleapis.com/maps/api/place/queryautocomplete/json'

# Create a dictionary containing the request parameters
values = dict()
values['input'] = 'North Quad'
values['key'] = '-- GOOGLE MAPS API KEY GOES HERE --' # ENTER YOUR API KEY HERE

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# Encode the dictionary into a Web-appropriate format
data = urllib.parse.urlencode(values)

# Attach the data to the URL
full_url = base_url + '?' + data # create full URL

# Request the URL
req = urllib.request.Request(full_url) # create URL lib request object to use in query

# Read the response into a Python string
response_str = None
with urllib.request.urlopen(req, context=ctx) as response: # calling Query Autocomplete service here!
	response_str = response.read().decode()

# Parse the response into a json object
json_response = json.loads(response_str)

# for result in json_response['predictions']:
#     if result['place_id'] == 'ChIJy_fxa0CuPIgRWmk6N0CQ0u8':
#         print (result['description'])

base_url2 = 'https://maps.googleapis.com/maps/api/place/details/json'
values2 = dict()
values2['place_id'] = '-- PLACE ID FOR NORTH QUADRANGLE GOES HERE --'
values2['key'] = '-- GOOGLE MAPS API KEY GOES HERE --'
data2 = urllib.parse.urlencode(values2)
full_url2 = base_url2 + '?' + data2
req2 = urllib.request.Request(full_url2)

with urllib.request.urlopen(req2, context=ctx) as response2:
    response_str2 = response2.read().decode()

json_response2 = json.loads(response_str2)

nqLat = json_response2['result']['geometry']['location']['lat']
nqLong = json_response2['result']['geometry']['location']['lng']

def makeLocationStr (lat, long):
    latStr = str(lat)
    longStr = str(long)
    return latStr + ',' + longStr

locationStr = makeLocationStr(nqLat, nqLong)
#print (locationStr)

print ('latitude = ' + str(nqLat) +
'  longitude = ' + str(nqLong))

# find restaurants within 500 meters of NQ
base_url3 = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json'
values3 = dict()
values3['key'] = '-- GOOGLE MAPS API KEY GOES HERE --'
values3['location'] = locationStr
values3['radius'] = 500
values3['type'] = 'restaurant'
data3 = urllib.parse.urlencode(values3)
full_url3 = base_url3 + '?' + data3
req3 = urllib.request.Request(full_url3)

with urllib.request.urlopen(req3, context=ctx) as response3:
    response_str3 = response3.read().decode()

json_response3 = json.loads(response_str3)

#print (json_response3)
resultsDict = {}

for result in json_response3['results']:
	if 'price_level' in result:
		price_level = result['price_level']
	else:
		price_level = 0
	resultsDict[result['name']] = (result['rating'], price_level)
	print (result['name'] + ' ' + str(result['rating']) + ' ' + str(price_level))

print (resultsDict)

resultsDict_items = resultsDict.items()
print (resultsDict_items)
userChoice = input("Would you like to sort the restaurants by rating or by price?\n" +
"Type 'rating' or 'price' --> ")

if userChoice.lower() == 'rating':
	sorted_by_rating = sorted(resultsDict_items, key = lambda x: x[1][0])
	for item in sorted_by_rating:
		print (item[0] + ' with rating of ' + str(item[1][0]))

elif userChoice.lower() == 'price':
	sorted_by_price = sorted(resultsDict_items, key = lambda x: x[1][1])
	for item in sorted_by_price:
		print (item[0] + ' with price level of ' + str(item[1][1]))
