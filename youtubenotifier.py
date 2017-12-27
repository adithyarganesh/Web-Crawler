<<<<<<< HEAD
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq
import requests

my_url = 'https://www.youtube.com/feed/trending?gl=US'

page = requests.get(my_url)
page_html = page.text

page_soup = soup(page_html, "html.parser")
containers = page_soup.findAll("li" , {"class":"expanded-shelf-content-item-wrapper"})

filename = "youtubescript.csv"
f = open(filename, "w")
headers = "Title, Time, Views \n"
f.write(headers)

for container in containers:
	x = container.findAll("div" , {"class": "yt-lockup-content"})
	title = x[0].h3.text
	print(title)

	y = container.findAll("ul" ,{ "class" : "yt-lockup-meta-info"})
	details = y[0].findAll("li")
	time = details[0].text
	views = details[1].text

	print("title" + title)
	print("time" + time)
	print("views" + views)



	f.write( title.replace(",", "|") +"," + time +"," + views.replace(",", " ") + "\n" )

f.close()


=======
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq
import requests

my_url = 'https://www.youtube.com/feed/trending?gl=US'

page = requests.get(my_url)
page_html = page.text

page_soup = soup(page_html, "html.parser")
containers = page_soup.findAll("li" , {"class":"expanded-shelf-content-item-wrapper"})

filename = "youtubescript.csv"
f = open(filename, "w")
headers = "Title, Time, Views \n"
f.write(headers)

for container in containers:
	x = container.findAll("div" , {"class": "yt-lockup-content"})
	title = x[0].h3.text
	print(title)

	y = container.findAll("ul" ,{ "class" : "yt-lockup-meta-info"})
	details = y[0].findAll("li")
	time = details[0].text
	views = details[1].text

	print("title" + title)
	print("time" + time)
	print("views" + views)



	f.write( title.replace(",", "|") +"," + time +"," + views.replace(",", " ") + "\n" )

f.close()


>>>>>>> b5928b6162417bf8e9efcc8fcb61a7562df0b8ff
