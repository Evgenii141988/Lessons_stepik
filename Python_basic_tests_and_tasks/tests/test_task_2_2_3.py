import pytest

from Python_basic_tests_and_tasks.task_2_2_3 import get_hex_string


@pytest.mark.parametrize('number, expected_result', [(35, "'0x23'"),
                                                     (54365, "'0xd45d'"),
                                                     (141, "'0x8d'"),
                                                     (1, "'0x1'"),
                                                     (2, "'0x2'"),
                                                     (16, "'0x10'"),
                                                     (17, "'0x11'")])
def test_func_get_hex_string(number, expected_result):
    assert get_hex_string(number) == expected_result


if __name__ == '__main__':
    pytest.main()
