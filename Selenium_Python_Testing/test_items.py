import pytest
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_check_button_add_to_basket(browser):
    browser.get(link)
    button_add_to_basket = browser.find_element(By.CSS_SELECTOR, ".btn-add-to-basket")
    assert button_add_to_basket.is_enabled(), 'WARNING!!! button add to basket is not found'


if __name__ == '__main__':
    pytest.main()
