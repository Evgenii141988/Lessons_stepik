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

        input_last_name = browser.find_element(By.NAME, 'lastname')
        input_last_name.send_keys('Ivanov')

        input_email = browser.find_element(By.NAME, 'email')
        input_email.send_keys('email@mail.ru')


        button = browser.find_element(By.CSS_SELECTOR, 'button.btn')
        button.click()

    finally:
        time.sleep(10)
        browser.quit()
