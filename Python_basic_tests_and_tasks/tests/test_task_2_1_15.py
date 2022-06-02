import pytest

from Python_basic_tests_and_tasks.task_2_1_15 import get_round_numbers, get_squad_numbers, get_add_previous_numbers


@pytest.mark.parametrize('numbers, expected_result', [([2.1, 3.5, 2.9, 3.1], [3, 4, 3, 4]),
                                                      ([1.2, 24.4, 35.2], [2, 25, 36]),
                                                      ([2.3, 9.23, 0.1, 99.2], [3, 10, 1, 100]),
                                                      ([0, 0, 0], [0, 0, 0]),
                                                      ([1, 2, 3], [1, 2, 3])])
def test_func_get_round_numbers(numbers, expected_result):
    assert get_round_numbers(numbers) == expected_result


@pytest.mark.parametrize('numbers, expected_result', [([2, 3, 2, 3], [4, 9, 4, 9]),
                                                      ([1, 24, 35], [1, 576, 1225]),
                                                      ([3, 10, 1, 100], [9, 100, 1, 10000]),
                                                      ([0, 0, 0], [0, 0, 0]),
                                                      ([1, 2, 3], [1, 4, 9])])
def test_func_get_squad_numbers(numbers, expected_result):
    assert get_squad_numbers(numbers) == expected_result


@pytest.mark.parametrize('numbers, expected_result', [([2, 3, 2, 3], [2, 5, 7, 10]),
                                                      ([4, 9, 16, 25], [4, 13, 29, 54]),
                                                      ([0, 0, 0], [0, 0, 0]),
                                                      ([1, 1, 1], [1, 2, 3]),
                                                      ([1, 2, 3, 4, 5, 6, 7, 8], [1, 3, 6, 10, 15, 21, 28, 36])])
def test_func_get_add_previous_numbers(numbers, expected_result):
    assert get_add_previous_numbers(numbers) == expected_result


if __name__ == '__main__':
    pytest.main()
