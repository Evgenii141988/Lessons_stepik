import pytest

from Python_basic_tests_and_tasks.task_2_1_13 import get_largest_simple_num, get_index_num, get_sum_digits


@pytest.mark.parametrize('numbers, expected_result', [([1, 2, 3, 5, 19], 19),
                                                      ([3, 11, 7, 17, 6, 4, 19], 19),
                                                      ([15, 4, 6, 9, 13, 89, 97, 25, 35, 124, 146], 97),
                                                      ([2, 3, 5, 7, 13, 11, 37, 61, 71, 83, 79], 83),
                                                      ([4, 6, 9, 15, 22, 44, 45, 35, 124, 146], 0),
                                                      ])
def test_func_get_largest_simple_num(numbers, expected_result):
    assert get_largest_simple_num(numbers) == expected_result


@pytest.mark.parametrize('numbers, number, expected_result', [([1, 2, 3, 5, 19], 19, 4),
                                                              ([3, 11, 7, 17, 6, 4, 19], 19, 6),
                                                              ([15, 4, 6, 9, 13, 89, 97, 25, 35, 124, 146], 97, 6),
                                                              ([2, 3, 5, 7, 13, 11, 37, 61, 71, 83, 79], 83, 9),
                                                              ([4, 6, 9, 15, 22, 44, 45, 35, 124, 146], 44, 5),
                                                              ])
def test_func_get_index_num(numbers, number, expected_result):
    assert get_index_num(numbers, number) == expected_result


@pytest.mark.parametrize('number, expected_result', [(1, 1), (19, 10), (142, 7), (35, 8), (20, 2)])
def test_func_get_sum_digits(number, expected_result):
    assert get_sum_digits(number) == expected_result


if __name__ == '__main__':
    pytest.main()
