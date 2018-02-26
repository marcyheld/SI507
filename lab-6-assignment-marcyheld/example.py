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
# with syntax !!!
# with open('f.txt') as file: # with ... as ... :
#  -- do this stuff --
# and automatically closes file after that indented block is executed
response_str = None
with urllib.request.urlopen(req, context=ctx) as response: # calling Query Autocomplete service here!
	response_str = response.read().decode()

# Parse the response into a json object
json_response = json.loads(response_str)

# Print the request status
print ('Request status:', json_response['status'])

# If available, print the predicted places
predictions = json_response.get('predictions', None)
if predictions:
	print ('Predicted places:')
	for place in predictions:
		print (place['description'])
