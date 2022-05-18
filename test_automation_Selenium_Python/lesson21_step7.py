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
        print(type(x))
    finally:
        time.sleep(10)
        browser.quit()
