from selenium import webdriver
from selenium.webdriver.common.by import By
import time

if __name__ == '__main__':

    link = "http://suninjuly.github.io/simple_form_find_task.html"

    try:
        browser = webdriver.Chrome()
        browser.get(link)

        input1 = browser.find_element(by=By.TAG_NAME, value="input")
        input1.send_keys("Ivan")
        input2 = browser.find_element(by=By.NAME, value="last_name")
        input2.send_keys("Petrov")
        input3 = browser.find_element(by=By.CLASS_NAME, value="city")
        input3.send_keys("Smolensk")
        input4 = browser.find_element(by=By.ID, value="country")
        input4.send_keys("Russia")
        button = browser.find_element(by=By.CSS_SELECTOR, value="button.btn")
        button.click()

    finally:
        # успеваем скопировать код за 30 секунд
        time.sleep(30)
        # закрываем браузер после всех манипуляций
        browser.quit()