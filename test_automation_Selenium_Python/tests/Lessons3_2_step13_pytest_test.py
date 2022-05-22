import pytest

from test_automation_Selenium_Python.lesson32_step13 import input_data


def test_reg1():
    assert input_data(
        "http://suninjuly.github.io/registration1.html") == "Congratulations! You have successfully registered!"


def test_reg2():
    assert input_data(
        "http://suninjuly.github.io/registration2.html") == "Congratulations! You have successfully registered!"


if __name__ == '__main__':
    pytest.main()
