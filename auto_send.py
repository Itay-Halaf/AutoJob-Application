import time
from selenium import webdriver
from bs4 import BeautifulSoup
import requests
from selenium.webdriver.common.by import By


options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options)

url = "https://www.alljobs.co.il/access.aspx?Camefrom=top_bar_login"
email = 'itayhalaf@gmail.com'


def html_to_text(url):
    website = requests.get(url)
    results = BeautifulSoup(website.text, 'html.parser')
    return results

def open_browser(url):
    #driver = webdriver.Chrome()
    driver.get(url)
    time.sleep(5.0)
    driver.find_element(By.ID,"inputEmail").send_keys(email)
    time.sleep(2.0)
    driver.close()
    #search_box = driver.find_element("name","inputEmail")
    #search_box.send_keys(email)
    #search_box.submit()

    #driver.send_keys(driver.findElement(By.id("inputEmail")))

def job_applicationer():
    #TODO
    return

def logInFunc():
    email = "itayhalaf@gmail.com"

    return

soup = html_to_text(url).prettify()
print(soup)
open_browser(url)