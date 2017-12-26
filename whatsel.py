from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by  import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

url = "https://www.premierleague.com/players"

browser = webdriver.Chrome('F:\exec\chromedriver.exe')
browser.get(url)

wait = WebDriverWait(browser, 60)

input_xpath = '//div[@class="input"][@dir="auto"][@data-tab="1"]'
input_element = wait.until(EC.presence_of_element_located((By.XPATH, input_xpath)))


elem = browser.find_element_by_tag_name("a")

no_of_pagedowns = 20

while no_of_pagedowns:
    elem.send_keys(Keys.PAGE_DOWN)
    time.sleep(0.2)
    no_of_pagedowns-=1

post_elems = browser.find_elements_by_class_name("post-item-title")

for post in post_elems:
    print (post.text)