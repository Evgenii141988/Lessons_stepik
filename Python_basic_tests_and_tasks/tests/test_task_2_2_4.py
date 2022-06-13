import pytest

from Python_basic_tests_and_tasks.task_2_2_4 import get_oct_number


@pytest.mark.parametrize('number, expected_result', [(35, 43),
                                                     (21, 25),
                                                     (141, 215),
                                                     (1, 1),
                                                     (2, 2),
                                                     (8, 10),
                                                     (9, 11)])
def test_func_get_oct_number(number, expected_result):
    assert get_oct_number(number) == expected_result


if __name__ == '__main__':
    pytest.main()