from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

if __name__ == '__main__':
    try:
        browser = webdriver.Chrome()
        link = 'http://suninjuly.github.io/alert_accept.html'
        browser.get(link)

        button_one = browser.find_element(By.CSS_SELECTOR, 'button.btn')
        button_one.click()

        confirm = browser.switch_to.alert
        confirm.accept()

    finally:
        time.sleep(10)
        browser.quit()
