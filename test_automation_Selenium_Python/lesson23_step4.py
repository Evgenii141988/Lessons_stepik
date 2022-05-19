from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

if __name__ == '__main__':
    try:
        browser = webdriver.Chrome()
        link = 'http://suninjuly.github.io/alert_accept.html'
        browser.get(link)
    finally:
        time.sleep(10)
        browser.close()