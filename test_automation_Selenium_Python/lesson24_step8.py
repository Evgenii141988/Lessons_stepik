from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

if __name__ == '__main__':
    try:
        browser = webdriver.Chrome()
        browser.get('http://suninjuly.github.io/explicit_wait2.html')
        flag = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, 'price'), '100'))
        button_book = browser.find_element(By.ID, 'book')
        if flag:
            button_book.click()



    finally:
        time.sleep(10)
        browser.quit()