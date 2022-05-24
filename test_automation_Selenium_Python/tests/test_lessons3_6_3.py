import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math


@pytest.fixture(scope='function')
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


# @pytest.fixture(scope="function")
# def answer():
#     return math.log(int(time.time()))

# @pytest.mark.parametrize('link', ['https://stepik.org/lesson/236895/step/1',
#                                   'https://stepik.org/lesson/236896/step/1',
#                                   'https://stepik.org/lesson/236897/step/1',
#                                   'https://stepik.org/lesson/236898/step/1',
#                                   'https://stepik.org/lesson/236899/step/1',
#                                   'https://stepik.org/lesson/236903/step/1',
#                                   'https://stepik.org/lesson/236904/step/1',
#                                   'https://stepik.org/lesson/236905/step/1'])
@pytest.mark.parametrize('link', ['https://stepik.org/lesson/236895/step/1'])
def test_get_answer(browser, link):
    try:
        browser.get(link)
        answer = math.log(int(time.time()))
        input_answer = WebDriverWait(browser, 12).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '.ember-text-area')))
        input_answer.send_keys(answer)
        button = WebDriverWait(browser, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'button.submit-submission')))
        button.click()
        browser.implicitly_wait(10)
        elem_with_text = WebDriverWait(browser, 12).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '.smart-hints__hint')))
        text_answer = elem_with_text.text
        assert text_answer == "Correct!", f'{text_answer}'
    except AssertionError as error:
        print(error.args[0])


if __name__ == '__main__':
    pytest.main()
