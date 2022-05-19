from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time


def calc(x: str) -> str:
    return str(math.log(abs(12 * math.sin(int(x)))))


if __name__ == '__main__':
    try:
        browser = webdriver.Chrome()
        link = 'http://suninjuly.github.io/alert_accept.html'
        browser.get(link)

        button_one = browser.find_element(By.CSS_SELECTOR, 'button.btn')
        button_one.click()

        confirm = browser.switch_to.alert
        confirm.accept()

        x_elm = browser.find_element(By.ID, 'input_value')
        x = x_elm.text
        y = calc(x)

        input_pole = browser.find_element(By.ID, 'answer')
        input_pole.send_keys(y)


    finally:
        time.sleep(10)
        browser.quit()
