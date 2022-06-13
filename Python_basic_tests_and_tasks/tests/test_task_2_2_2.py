import pytest

from Python_basic_tests_and_tasks.task_2_2_2 import get_correct_number


@pytest.mark.parametrize('number, expected_result', [(1425, True),
                                                     (1234, True),
                                                     (1221, False),
                                                     (1000, False),
                                                     (1001, False),
                                                     (2222, True),
                                                     (5689, True)])
def test_func_get_correct_number(number, expected_result):
    assert get_correct_number(number) == expected_result


if __name__ == '__main__':
    pytest.main()
