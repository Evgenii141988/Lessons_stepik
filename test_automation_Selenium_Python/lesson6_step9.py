from selenium import webdriver
from selenium.webdriver.common.by import By
import time

if __name__ == '__main__':
    link = 'http://suninjuly.github.io/registration1.html'
    brawser = webdriver.Chrome()
    brawser.get(link)
    try:
        input_first_name = brawser.find_element(By.CSS_SELECTOR, 'div.first_block .first')
        input_first_name.send_keys('Ivan')
        input_last_name = brawser.find_element(By.CSS_SELECTOR, 'div.first_block .second')
        input_last_name.send_keys('Ivanov')
        input_email = brawser.find_element(By.CSS_SELECTOR, 'div.first_block .third')
        input_email.send_keys('ivan_ivanov@mail.ru')
        button = brawser.find_element(By.CSS_SELECTOR, 'button.btn')
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elm = brawser.find_element(By.TAG_NAME, 'h1')
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elm.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        assert "Congratulations! You have successfully registered!" == welcome_text
    finally:
        time.sleep(10)
        brawser.quit()
