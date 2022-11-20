import time
from selenium import webdriver
from selenium.webdriver.common.by import by
from bs4 import BeautifulSoup as bs
import os

print (os.path.abspath(os.getcwd()))

chrome_driver_path = 'C:\Users\itayh\OneDrive\שולחן העבודה\All Jobs Auto Sender\chrom_driver\chromedriver.exe'
driver = webdriver.Chrome(executable_path=chrome_driver_path)


def logInFunc():
    url = "https://www.alljobs.co.il/access.aspx?Camefrom=top_bar_login"
    email = "itayhalaf@gmail.com"
    driver.get(url)
    time.sleep(5.0)
    userNameBox = driver.find_element_by_xpath(by =By.ID, value = '//*[@id="email-text-box"]')
    if (len(userNameBox) > 0):
        userNameBox.click()
        userNameBox.send_keys(email)
    else:
        print("Err -1")
        return
logInFunc()