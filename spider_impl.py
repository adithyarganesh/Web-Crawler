import urllib
from urllib.parse import urljoin
from bs4 import BeautifulSoup as soup
import requests
url = 'http://www.yahoo.com'

urls = [url]
visited = [url]
i=0
while len(urls) > i :
	#try: 
	page = requests.get(urls[i])
	page_html = page.text
	soup = soup(page_html, 'html.parser')
#except:
	print (urls[0])
	i +=1

	urls.pop()
	print (len(urls))

	for tag in soup.findAll('a', href = true):
		tag['href'] = urlparse.urljoin(url, tag['href'])
		if url in tag['href'] and tag['href'] not in visited:
			urls.append(tag['href'])
			visited.append(tag['href'])

print (visited)
