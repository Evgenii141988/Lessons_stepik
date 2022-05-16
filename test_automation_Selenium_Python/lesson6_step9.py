from selenium import webdriver
from selenium.webdriver.common.by import By
import time

if __name__ == '__main__':
    link = 'http://suninjuly.github.io/registration1.html'
    brawser = webdriver.Chrome()
    brawser.get(link)
    try:
        pass
    except Exception as ex:
        print(ex)
    finally:
        time.sleep(10)
        brawser.quit()