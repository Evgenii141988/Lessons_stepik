import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

@pytest.fixture(scope='Function')
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@pytest.mark.parametrize('link', ['https://stepik.org/lesson/236895/step/1',
                                    'https://stepik.org/lesson/236896/step/1',
                                    'https://stepik.org/lesson/236897/step/1',
                                    'https://stepik.org/lesson/236898/step/1',
                                    'https://stepik.org/lesson/236899/step/1',
                                    'https://stepik.org/lesson/236903/step/1',
                                    'https://stepik.org/lesson/236904/step/1',
                                    'https://stepik.org/lesson/236905/step/1'])
def test_get_answer(browser, link):
    pass
