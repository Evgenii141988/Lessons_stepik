from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os


if __name__ == '__main__':
    try:
        browser = webdriver.Chrome()
        link = 'http://suninjuly.github.io/file_input.html'
        browser.get(link)

    finally:
        time.sleep(10)
