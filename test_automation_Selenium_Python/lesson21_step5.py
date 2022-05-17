from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time


def calc(x: str) -> str:
    return str(math.log(abs(12 * math.sin(int(x)))))


if __name__ == '__main__':
    try:
        browser = webdriver.Chrome()
        link = 'http://suninjuly.github.io/math.html'
        browser.get(link)
        x_element = browser.find_element(By.CSS_SELECTOR, '#input_value')
        x = x_element.text
        y = calc(x)
        input_text = browser.find_element(By.CSS_SELECTOR, '#answer')
        input_text.send_keys(y)
        my_checkbox = browser.find_element(By.CSS_SELECTOR, '#robotCheckbox')
        my_checkbox.click()
        my_radiobutton = browser.find_element(By.CSS_SELECTOR, '#robotsRule')
        my_radiobutton.click()
        button = browser.find_element(By.CSS_SELECTOR, 'button.btn')
        button.click()
    except Exception as ex:
        print(ex)
    finally:
        time.sleep(10)
        browser.quit()
