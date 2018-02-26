import wikipedia
from bs4 import BeautifulSoup

hpPage = wikipedia.page("Harry Potter")
hpPagehtml = hpPage.html()
#print (hpPagehtml)

hpSoup = BeautifulSoup(hpPagehtml, "html.parser")
#print (hpSoup)

def print_section_titles(wikiSoupObj):
    allThings = wikiSoupObj.find_all("span", class_="mw-headline")
    count = 1
    print("Section Titles")
    for thing in allThings:
        print (str(count) + ' ' + thing.get_text())
        count += 1

def print_references(wikiSoupObj):
    allThings = wikiSoupObj.find_all("span", class_="reference-text")
    count = 1
    print ("References")
    for thing in allThings:
        print (str(count) + ' ' + thing.get_text())
        count += 1

def interactive_wiki():
    # user enters search term, term is searched on Wikipedia
    userTerm = input('Enter a search term --> ')
    searchResults = wikipedia.search(userTerm)

    # display ordered list of results of Wikipedia search
    count = 0
    for item in searchResults:
    	print (str(count) + ' ' + item)
    	count += 1

    userChoice = input("Select the page u want --> ")
    # go to the index position in search results list that matches the
    # user choice
    page = wikipedia.page(searchResults[int(userChoice)])
    pageHTML = page.html()
    userSoup = BeautifulSoup(pageHTML, "html.parser")

    print_section_titles(userSoup)
    print("\n\n")
    print_references(userSoup)

# print (type(print_section_titles(hpSoup)))
# print (print_section_titles(hpSoup))
# print_section_titles(hpSoup)
# print_references(hpSoup)
interactive_wiki()
