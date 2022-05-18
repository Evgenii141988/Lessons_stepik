from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os


if __name__ == '__main__':
    try:
        browser = webdriver.Chrome()
        link = 'http://suninjuly.github.io/file_input.html'
        browser.get(link)

        input_first_name = browser.find_element(By.NAME, 'firstname')
        input_first_name.send_keys('Ivan')
    finally:
        time.sleep(10)
