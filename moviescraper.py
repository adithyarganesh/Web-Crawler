<<<<<<< HEAD
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq

import requests

my_url = 'https://fmovies.is/'

page = requests.get(my_url)
page_html = page.text

page_soup = soup(page_html, "html.parser")
containers = page_soup.findAll("div" , {"class":"col-lg-3 col-md-4 col-sm-6 col-xs1-8 col-xs-12"})

filename = "moviescript.csv"
f = open(filename, "w")
headers = "Title, episode \n"
f.write(headers)

for container in containers:
	x = container.findAll("a" , {"class" : "name"})
	title = x[0].text
	print(title)

	ep = container.findAll("div" , {"class" : "status"})
	try :
		episode = ep[0].span.text
	except :
		episode = ""
	print(episode)
	f.write( title.replace(",", "|") +"," + episode +  ",\n" )

f.close()


=======
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq

import requests

my_url = 'https://fmovies.is/'

page = requests.get(my_url)
page_html = page.text

page_soup = soup(page_html, "html.parser")
containers = page_soup.findAll("div" , {"class":"col-lg-3 col-md-4 col-sm-6 col-xs1-8 col-xs-12"})

filename = "moviescript.csv"
f = open(filename, "w")
headers = "Title, episode \n"
f.write(headers)

for container in containers:
	x = container.findAll("a" , {"class" : "name"})
	title = x[0].text
	print(title)

	ep = container.findAll("div" , {"class" : "status"})
	try :
		episode = ep[0].span.text
	except :
		episode = ""
	print(episode)
	f.write( title.replace(",", "|") +"," + episode +  ",\n" )

f.close()


>>>>>>> b5928b6162417bf8e9efcc8fcb61a7562df0b8ff
