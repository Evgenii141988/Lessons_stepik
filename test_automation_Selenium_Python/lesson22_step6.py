from selenium import webdriver
from selenium.webdriver.common.by import By
import time


if __name__ == '__main__':
    try:
        browser = webdriver.Chrome()
        link = "https://SunInJuly.github.io/execute_script.html"
        browser.get(link)
        button = browser.find_element(By.TAG_NAME, 'button')
    # except Exception as ex:
    #     print(ex)
    finally:
        time.sleep(10)
        browser.quit()
