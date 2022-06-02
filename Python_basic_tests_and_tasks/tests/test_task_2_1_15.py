import pytest

from Python_basic_tests_and_tasks.task_2_1_15 import get_round_numbers


@pytest.mark.parametrize('numbers, expected_result', [([2.1, 3.5, 2.9, 3.1], [3, 4, 3, 4]),
                                                      ([1.2, 24.4, 35.2], [2, 25, 36]),
                                                      ([2.3, 9.23, 0.1, 99.2], [3, 10, 1, 100]),
                                                      ([0, 0, 0], [0, 0, 0]),
                                                      ([1, 2, 3], [1, 2, 3])])
def test_func_get_round_numbers(numbers, expected_result):
    assert get_round_numbers(numbers) == expected_result


if __name__ == '__main__':
    pytest.main()
