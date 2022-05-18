from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x: str) -> str:
    return str(math.log(abs(12 * math.sin(int(x)))))


if __name__ == '__main__':
    try:
        browser = webdriver.Chrome()
        link = "http://suninjuly.github.io/execute_script.html"
        browser.get(link)

        x_elem = browser.find_element(By.ID, 'input_value')
        x = x_elem.text
        y = calc(x)

        button = browser.find_element(By.TAG_NAME, 'button')
        button.click()
    except Exception as ex:
        print(ex)
    finally:
        time.sleep(10)
        browser.quit()
