from selenium import webdriver
from selenium.webdriver.common.by import By
import time

if __name__ == '__main__':
    link = 'http://suninjuly.github.io/registration1.html'
    brawser = webdriver.Chrome()
    brawser.get(link)
    try:
        input1 = brawser.find_element(By.CLASS_NAME, 'first')
        input1.send_keys('Ivan')
        input2 = brawser.find_element(By.CLASS_NAME, 'second')
        input2.send_keys('Ivanov')
    except Exception as ex:
        print(ex)
    finally:
        time.sleep(10)
        brawser.quit()