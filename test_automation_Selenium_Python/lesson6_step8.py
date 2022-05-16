from selenium import webdriver
from selenium.webdriver.common.by import By
import time

if __name__ == '__main__':
    link = 'http://suninjuly.github.io/find_xpath_form'
    try:
        browser = webdriver.Chrome()
        browser.get(link)
        input1 = browser.find_element(By.TAG_NAME, 'input')
        input1.send_keys('Ivan')
    except Exception as ex:
        print(ex)
    finally:
        time.sleep(30)
        browser.quit()