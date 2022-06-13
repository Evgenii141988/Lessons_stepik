import pytest

from Python_basic_tests_and_tasks.task_2_2_1 import get_binary_number


@pytest.mark.parametrize('number, expected_result', [(35, 100011),
                                                     (21, 10101),
                                                     (141, 10001101),
                                                     (2, 10),
                                                     (3, 11),
                                                     (4, 100),
                                                     (5, 101),
                                                     (1, 1)])
def test_func_get_binary_number(number, expected_result):
    assert get_binary_number(number) == expected_result


if __name__ == '__main__':
    pytest.main()
