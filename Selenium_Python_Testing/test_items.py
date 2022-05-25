import pytest
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_check_button_add_to_basket(browser):
    browser.get(link)
    button_add_to_basket = browser.find_element(By.CSS_SELECTOR, ".btn-add-to-basket")
    name_button = button_add_to_basket.text
    assert name_button == 'Añadir al carrito', 'Language is not español'


if __name__ == '__main__':
    pytest.main()
