from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

if __name__ == '__main__':
    try:
        browser = webdriver.Chrome()
        link = 'http://suninjuly.github.io/redirect_accept.html'
        browser.get(link)

        button_one = browser.find_element(By.CSS_SELECTOR, 'button.trollface')
        button_one.click()

    finally:
        time.sleep(10)
        browser.quit()