from selenium import webdriver
from selenium.webdriver.common.by import By
import time

if __name__ == '__main__':
    link = 'http://suninjuly.github.io/registration1.html'
    brawser = webdriver.Chrome()
    brawser.get(link)
    try:
        input_first_name = brawser.find_element(By.CLASS_NAME, 'first')
        input_first_name.send_keys('Ivan')
        input_last_name = brawser.find_element(By.CLASS_NAME, 'second')
        input_last_name.send_keys('Ivanov')
        input_email = brawser.find_element(By.CLASS_NAME, 'third')
        input_email.send_keys('ivan_ivanov@mail.ru')

    except Exception as ex:
        print(ex)
    finally:
        time.sleep(10)
        brawser.quit()