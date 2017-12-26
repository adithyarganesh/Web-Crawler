from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by  import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException as nsee
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException as texc
import sys
import errno
import socket
from socket import error as socket_error

def is_connected(host="8.8.8.8", port=53, timeout=10):
    try:
        socket.setdefaulttimeout(timeout)
        socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((host,port))
        return True
    except Exception as ex:
        print (ex.message)
        return (False)
def login(driver, user, pw):
    if not is_connected():
        print ("Not connected to the network")
        return (None)
    try:
        user_name = driver.find_element_by_name("email")
        pwd = driver.find_element_by_name("pass")
        user_name.clear()
        user_name.send_keys(user)
        pwd.send_keys(pw)
        pwd.send_keys(Keys.RETURN)
    except nsee:
        print ("It seems you are not on the same page!!")

# A function to logout the user
# @param driver is the webdriver
def logout(driver):
    if not is_connected():
        print ("Not connected to the network")
        return (None)
    try:
        dropdown = driver.find_element_by_id("userNavigationLabel")
        dropdown.click()
        driver.find_element_by_xpath("//span[contains(@class, '_54nh') and contains(text(), 'Log out')]").click()
    except nsee:
        print ("It seems you are not on the same page!!")

def main():
    if not is_connected():
        print ("Not connected to the internet")
        return (None)
    driver = webdriver.Chrome('F:\exec\chromedriver.exe')
    driver.implicitly_wait(10)
    driver.get("https://www.facebook.com/")
    print ("1. login <user_name> <password>")
    print ("2. logout")
    print ("3. quit")
    isLoggedIn = False
    # Emulate do while
    while True:
        cmd = raw_input()
        cmd_list = cmd.split(' ')
        cm = cmd_list[0]
        if cm == 'login':
            if not len(cmd_list) == 3 :
                print ("Incorrect use of login command")
            elif isLoggedIn:
                print ("Already logged in")
            else:
                try:
                    login(driver,cmd_list[1], cmd_list[2])
                    isLoggedIn = True
                    print ("Logged in I guess")
                except socket_error as serr:
                    if serr.errno != errno.ECONNREFUSED:
                        raise serr
                    else:
                        print ("Closed the tab already")
        elif cm == 'logout':
            if not isLoggedIn:
                print ("Can't log out if you aren't logged in!!")
            else:
                logout(driver)
                isLoggedIn = False
                print ("Logged out I guess")
        elif cm == 'quit':
            print ("Closing and quitting ...")
            try:
                driver.close()
            except socket_error as serr:
                if serr.errno != errno.ECONNREFUSED:
                    raise serr
                else:
                    print ("Closed the tab already")
            break
        else:
            print ("Invalid command")
            
    
if __name__ == '__main__':
    main()