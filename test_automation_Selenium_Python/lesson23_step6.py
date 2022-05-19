from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x: str) -> str:
    return str(math.log(abs(12 * math.sin(int(x)))))


if __name__ == '__main__':
    try:
        browser = webdriver.Chrome()
        link = 'http://suninjuly.github.io/redirect_accept.html'
        browser.get(link)

        button_one = browser.find_element(By.CSS_SELECTOR, 'button.trollface')
        button_one.click()

        new_window = browser.window_handles[1]
        browser.switch_to.window(new_window)

        x_elm = browser.find_element(By.ID, 'input_value')
        x = x_elm.text
        y = calc(x)


    finally:
        time.sleep(10)
        browser.quit()
