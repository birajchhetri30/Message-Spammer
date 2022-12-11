from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import getpass


def openBrowser():
    PATH = "C:/Users/Lenovo/Downloads/Compressed/chromedriver"
    driver = webdriver.Chrome(PATH)
    driver.get("https://www.messenger.com/")
    time.sleep(3)
    return driver


def login():
    driver = openBrowser()

    name = input('Enter username: ')
    search = driver.find_element("name", "email")
    search.send_keys(name)

    password = getpass.getpass()
    search = driver.find_element("name", "pass")
    search.send_keys(password)

    search.send_keys(Keys.RETURN)

    time.sleep(5)

    a = input('Please select a chat. Press ENTER when done: ')

    #time.sleep(5)
    #driver.find_element(By.XPATH, '//button[normalize-space()="Not Now"]').click()

    time.sleep(5)
    search = driver.find_element(By.CSS_SELECTOR, 'div[aria-describedby]')

    return search


def spam(textArea):
    file = open("shrek.txt", encoding="utf8")

    for line in file:
        textArea.send_keys(line)
        textArea.send_keys(Keys.RETURN)

    time.sleep(10)
    return textArea


if __name__ == '__main__':
    textArea = login()
    textArea = spam(textArea)