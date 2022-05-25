import pytest
from selenium.webdriver.common.by import By
import time

# link = "http://selenium1py.pythonanywhere.com/"
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_guest_should_see_login_link_pass(browser):
    browser.get(link)
    browser.find_element(By.CSS_SELECTOR, "#login_link")
    time.sleep(10)


# def test_guest_should_see_login_link_fail(browser):
#     browser.get(link)
#     browser.find_element(By.CSS_SELECTOR, "#magic_link")


if __name__ == '__main__':
    pytest.main()


# Проверяем команды в терминале:
# pytest -v --tb=line --reruns 1 --browser_name=chrome test_rerun.py
# pytest --language=es test_rerun.py