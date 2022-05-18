from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time


if __name__ == '__main__':
    try:
        browser = webdriver.Chrome()
        link = 'http://suninjuly.github.io/selects1.html'
        browser.get(link)
        num_a = browser.find_element(By.ID, 'num1')
        a = int(num_a.text)
        num_b = browser.find_element(By.ID, 'num2')
        b = int(num_b.text)

    finally:
        time.sleep(10)
