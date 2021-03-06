from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time


def calc(x: str) -> str:
    return str(math.log(abs(12 * math.sin(int(x)))))


if __name__ == '__main__':
    try:
        browser = webdriver.Chrome()
        link = 'http://suninjuly.github.io/get_attribute.html'
        browser.get(link)
        x_elem = browser.find_element(By.ID, 'treasure')
        x = x_elem.get_attribute('valuex')
        y = calc(x)
        input_y = browser.find_element(By.ID, 'answer')
        input_y.send_keys(y)
        chech_box = browser.find_element(By.ID, 'robotCheckbox')
        chech_box.click()
        rd_btn = browser.find_element(By.ID, 'robotsRule')
        rd_btn.click()
        button = browser.find_element(By.CSS_SELECTOR, 'button.btn')
        button.click()
    finally:
        time.sleep(10)
        browser.quit()
