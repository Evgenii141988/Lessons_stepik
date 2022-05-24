import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math
# from test_automation_Selenium_Python.conftest import browser


# @pytest.fixture(scope='function')
# def browser():
#     driver = webdriver.Chrome()
#     yield driver
#     driver.quit()


final_answer = []


@pytest.mark.parametrize('link', ['https://stepik.org/lesson/236895/step/1',
                                  'https://stepik.org/lesson/236896/step/1',
                                  'https://stepik.org/lesson/236897/step/1',
                                  'https://stepik.org/lesson/236898/step/1',
                                  'https://stepik.org/lesson/236899/step/1',
                                  'https://stepik.org/lesson/236903/step/1',
                                  'https://stepik.org/lesson/236904/step/1',
                                  'https://stepik.org/lesson/236905/step/1'])
def test_get_answer(browser, link):
    browser.get(link)
    answer = math.log(int(time.time()))

    input_answer = WebDriverWait(browser, 12).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '.ember-text-area')))
    input_answer.send_keys(answer)

    button = WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, 'button.submit-submission')))
    button.click()

    elem_with_text = WebDriverWait(browser, 12).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '.smart-hints__hint')))
    text_answer = elem_with_text.text
    try:
        assert text_answer == "Correct!", f'Here is the code: {text_answer}'
    except AssertionError:
        final_answer.append(text_answer)
    finally:
        print(*final_answer, sep='')


if __name__ == '__main__':
    pytest.main()
