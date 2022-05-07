# Дано число n. С начала суток прошло n минут. Определите, сколько часов и минут будут показывать
# электронные часы в этот момент.
# Программа должна вывести два числа: количество часов (от 0 до 23) и количество минут (от 0 до 59).
# Учтите, что число n может быть больше, чем количество минут в сутках.

def get_days(n: int) -> int:
    return n // (24 * 60)


def get_hours(n: int) -> int:
    return (n - get_days(n) * 24 * 60) // 60


def get_minutes(n: int) -> int:
    return (n - get_days(n) * 24 * 60) % 60


if __name__ == '__main__':
    n = int(input())
    print(get_hours(n), get_minutes(n))
