#proj2.py

# Marcy Held
# SI 507
# 23 Feb 2017

from bs4 import BeautifulSoup
import urllib.parse, urllib.request
import ssl

#### Problem 1 ####
print('\n*********** PROBLEM 1 ***********')
print('New York Times -- First 10 Story Headings\n')

### Your Problem 1 solution goes here
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

nyt_html = urllib.request.urlopen('http://nytimes.com', context=ctx).read()
nytSoup = BeautifulSoup(nyt_html, 'html.parser')
title_list = []
for title_words in nytSoup.find_all(class_="story-heading"):
    for words in title_words.find_all('a'):
        title_list.append(words.get_text().strip())

for i in range(10):
    print (title_list[i])

#### Problem 2 ####
print('\n*********** PROBLEM 2 ***********')
print('Michigan Daily -- MOST READ\n')

### Your Problem 2 solution goes here
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

mich_html = urllib.request.urlopen('https://www.michigandaily.com/', context=ctx).read()
michSoup = BeautifulSoup(mich_html, 'html.parser')

for stuff in michSoup.find_all(class_="view-id-most_read"):
    for item in stuff.find_all("a"):
        print (item.get_text())

#### Problem 3 ####
print('\n*********** PROBLEM 3 ***********')
print("Mark's page -- Alt tags\n")

### Your Problem 3 solution goes here
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

mark_html = urllib.request.urlopen('http://newmantaylor.com/gallery.html', context=ctx).read()
markSoup = BeautifulSoup(mark_html, 'html.parser')

for thing in markSoup.find_all('img'):
    if thing.get('alt') == None:
        print("No alternative text provided!")
    else:
        print(thing.get('alt'))

#### Problem 4 ####
print('\n*********** PROBLEM 4 ***********')
print("UMSI faculty directory emails\n")

### Your Problem 4 solution goes here
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

base_url = 'https://www.si.umich.edu/directory?field_person_firstname_value=&field_person_lastname_value=&rid=4'
faculty_req = urllib.request.Request(base_url, None, {'User-Agent': 'SI_CLASS'})
faculty_html = urllib.request.urlopen(faculty_req, context=ctx)
facultySoup = BeautifulSoup(faculty_html, 'html.parser')

# create list to hold URLs that lead to each prof's page
urlList = []

# get info from first page and URL for page 2
for stuff in facultySoup.find_all(class_= "field-item even"):
    for item in stuff.find_all('a'):
        if item.get_text() == "Contact Details":
            urlList.append('https://www.si.umich.edu' + item.get('href'))

for stuff in facultySoup.find_all(class_="pager-next"):
    for item in stuff.find_all('a'):
        nextURL = ('https://si.umich.edu' + item.get('href'))

# use nextURL to access page 2, and then 3-6
# append all link to each prof's page to urlList
for i in range(5):
    faculty_req = urllib.request.Request(nextURL, None, {'User-Agent': 'SI_CLASS'})
    faculty_html = urllib.request.urlopen(faculty_req, context=ctx)
    facultySoup = BeautifulSoup(faculty_html, 'html.parser')

    for stuff in facultySoup.find_all(class_= "field-item even"):
        for item in stuff.find_all('a'):
            if item.get_text() == "Contact Details":
                urlList.append('https://www.si.umich.edu' + item.get('href'))

    for stuff in facultySoup.find_all(class_="pager-next"):
        for item in stuff.find_all('a'):
            nextURL = ('https://si.umich.edu' + item.get('href'))

# use all links in urlList to travel to each prof's page
# once on prof's page, find the email address
# print the corresponding count and email address to the console
count = 1
for link in urlList:
    indiv_req = urllib.request.Request(link, None, {'User-Agent': 'SI_CLASS'})
    indiv_html = urllib.request.urlopen(indiv_req, context=ctx)
    indivSoup = BeautifulSoup(indiv_html, 'html.parser')
    for stuff in indivSoup.find_all(class_="field-type-email"):
        for item in stuff.find_all('a'):
            print (str(count) + " " + item.get_text())
        count += 1
