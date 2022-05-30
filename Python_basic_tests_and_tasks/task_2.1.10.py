from math import pi


def get_circle_square(r: float) -> float:
    return pi * r ** 2


if __name__ == '__main__':
    R = float(input())
    print(get_circle_square(R))