import pytest

from Python_basic_tests_and_tasks.task_2_1_12 import get_max_negative_num, get_min_positive_num


@pytest.mark.parametrize('numbers, expected_result', [([9, 8, 2, -3, -9, -1], -1),
                                                      ([-1, -2, -5, -9], -1),
                                                      ([1, 4, 5], 0)])
def test_get_max_negative_num(numbers, expected_result):
    assert get_max_negative_num(numbers) == expected_result


@pytest.mark.parametrize('numbers, expected_result', [([9, 8, 2, -3, -9, -1], 2),
                                                      ([-1, -2, -5, -9], 0),
                                                      ([1, 4, 5], 1)])
def test_get_min_positive_num(numbers, expected_result):
    assert get_min_positive_num(numbers) == expected_result


if __name__ == '__main__':
    pytest.main()