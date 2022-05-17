from selenium import webdriver
from selenium.webdriver.common.by import By
import math


def calc(x: str) -> str:
    return str(math.log(abs(12 * math.sin(int(x)))))


if __name__ == '__main__':
    browser = webdriver.Chrome()
    link = 'http://suninjuly.github.io/math.html'
    browser.get(link)
    x_element = browser.find_element(By.CSS_SELECTOR, '#input_value')
    x = x_element.text
    y = calc(x)
    input_text = browser.find_element(By.CSS_SELECTOR, '#answer')
    input_text.send_keys(y)