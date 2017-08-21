from bs4 import BeautifulSoup as soup
import requests

url = 'http://www.ssn.edu.in/'

page = requests.get(url)
page_html = page.text
page_soup = soup(page_html , 'html.parser')
filename = "ssn_spider.csv"
f = open(filename, "w")
headers = "Link \n"
f.write(headers)

link = page_soup.findAll('a')
i = 0
while i < 50 :
	print (link[i].get('href'))
	f.write(link[i].get('href') + "\n")
	i += 1
f.close()