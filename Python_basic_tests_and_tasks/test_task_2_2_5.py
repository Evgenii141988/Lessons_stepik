import pytest

from Python_basic_tests_and_tasks.task_2_2_6 import get_mult_five_first_number


@pytest.mark.parametrize('number1, number2, expected_result', [(2, 15, (2, 15)),
                                                               (-15, 6, (-75, 6))])
def test_func_get_mult_five_first_number(number1, number2, expected_result):
    assert get_mult_five_first_number(number1, number2) == expected_result


if __name__ == '__main__':
    pytest.main()
