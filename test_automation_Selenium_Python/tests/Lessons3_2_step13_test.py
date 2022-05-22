from unittest import TestCase, main
from test_automation_Selenium_Python.lesson32_step13 import input_data


class TestFormRegistration(TestCase):
    def test_reg1(self):
        self.assertEqual(input_data("http://suninjuly.github.io/registration1.html"),
                         "Congratulations! You have successfully registered!")

    def test_reg2(self):
        self.assertEqual(input_data("http://suninjuly.github.io/registration2.html"),
                         "Congratulations! You have successfully registered!")


if __name__ == '__main__':
    main()
