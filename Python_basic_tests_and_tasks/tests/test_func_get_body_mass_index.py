import pytest

from Python_basic_tests_and_tasks.task_2_1_11 import get_body_mass_index


@pytest.mark.parametrize('m, h, expected_result', [(58, 2, 14.5),
                                                   (38.2, 1.12, 30.45),
                                                   (94, 1.51, 41.23)])
def test_func_body_mass_index(m, h, expected_result):
    assert get_body_mass_index(m, h) == expected_result


if __name__ == '__main__':
    pytest.main()
