#its a program that collects data from a website or page

import requests
#module to get and request a request
from bs4 import BeautifulSoup
#beautifulsoup module lets program to see through website source and allows to grab data from the website

def spider(max_pages):#paramter max page is passed so that we can specify the no. of pages of website we want to crawl
    page = 1
    while page <= max_pages:
        url = "https://www.amazon.in/s?k=phones&ref=nb_sb_noss" + str(page) #the url we want to crawl and the incremented page no.
        source_code = requests.get(url) #each time loops, program will connect to webpage then store in variable source_code
        #theres a lot of data, inclusive of what user doesnt want so we add next line
        plain_text = source_code.text
        #beautifulsoup module or class needs a beautifulsoup object created to grad data correctly
        soup = BeautifulSoup(plain_text)#this line creates a soup object for the plain source code we created
        #looking for all the links, titles etc
        #like if we want to grab only the titles of each item on a website page this object would make it easy as we can search according to the class of that specific item
        for link in soup.findAll('a' , { 'class' : 'item-name' }): #"a" is used for linking in html the ahref tag, find all the links with the class item-name - here item name is the class for the title of every item of the website url we have provided
            #this is how beautifulsoup will be able to grab the titles
            href = link.get('href') #so that we can get the url link for every object of that specific item-name
            fullhref = "https://www,amazon.in" + href #the url obtained by href is just the item-name url only - contained within the 'phone' directory of the website we are using
            #for forming the complete url we would basically need the url till the phone directory forming a complete url
            #this would form a working url
            title = link.string
            #in the a tag - the text not set as any tag is the parameter string - which contains the actual title of the item
            print(fullhref)
            print(title)
        page+=1#to shift to next page for the next turn





