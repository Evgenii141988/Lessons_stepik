import pytest
from selenium.common.exceptions import NoSuchElementException


from test_automation_Selenium_Python.lesson32_step13 import input_data


def test_reg1():
    assert input_data(
        "http://suninjuly.github.io/registration1.html") == "Congratulations! You have successfully registered!"


def test_reg2():
    assert input_data(
        "http://suninjuly.github.io/registration2.html") == "Congratulations! You have successfully registered!"

def test_for_exception():
    with pytest.raises(NoSuchElementException):
        input_data("http://suninjuly.github.io/registration2.html")
        pytest.fail(f'Не найден элемент last_name')


if __name__ == '__main__':
    pytest.main()
