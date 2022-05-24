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

@pytest.fixture(scope="function")
def answer():
    return math.log(int(time.time()))

@pytest.mark.parametrize('link', ['https://stepik.org/lesson/236895/step/1',
                                  'https://stepik.org/lesson/236896/step/1',
                                  'https://stepik.org/lesson/236897/step/1',
                                  'https://stepik.org/lesson/236898/step/1',
                                  'https://stepik.org/lesson/236899/step/1',
                                  'https://stepik.org/lesson/236903/step/1',
                                  'https://stepik.org/lesson/236904/step/1',
                                  'https://stepik.org/lesson/236905/step/1'])
# @pytest.mark.parametrize('link', ['https://stepik.org/lesson/236895/step/1'])
def test_get_answer(browser, link):
    try:
        browser.get(link)
        browser.implicitly_wait(10)
        input_answer = browser.find_element(By.CLASS_NAME, 'ember-text-area')
        # input_answer = WebDriverWait(browser, 5).until(EC.element_located_to_be_selected((By.CLASS_NAME, 'ember-text-area')))
        answer = math.log(int(time.time()))
        input_answer.send_keys(answer)
        button = browser.find_element(By.CSS_SELECTOR, 'button.submit-submission')
        # button = WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button.submit-submission')))
        button.click()
        browser.implicitly_wait(10)
        elem_with_text = browser.find_element(By.CLASS_NAME, 'smart-hints__hint')
        text_answer = elem_with_text.text
        assert text_answer == "Correct!", f'{text_answer}'
    except AssertionError as error:
        print(error.args[0])


if __name__ == '__main__':
    pytest.main()
