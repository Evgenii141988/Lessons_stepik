from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

if __name__ == '__main__':
    try:
        browser = webdriver.Chrome()
        browser.get('http://suninjuly.github.io/explicit_wait2.html')
    finally:
        time.sleep(10)