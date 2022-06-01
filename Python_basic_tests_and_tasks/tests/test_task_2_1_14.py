import pytest

from Python_basic_tests_and_tasks.task_2_1_14 import get_two_closest_nums


@pytest.mark.parametrize('numbers, expected_result', [([3.1, 4.5, 2.8, 2.71], (2.71, 2.8)),
                                                      ([6.1, 4.3, 7.2, 6.3, 9.3], (6.1, 6.3)),
                                                      ([12.01, 23.51, 22.52, 12.31, 22.52], (12.01, 12.31)),
                                                      ])
def test_func_get_two_closest_nums(numbers, expected_result):
    assert get_two_closest_nums(numbers) == expected_result


if __name__ == '__main__':
    pytest.main()
