# На вход подаются два целых числа N и M. Напишите программу,
# которая умножает первое число на 5, если оно больше второго по абсолютной величине.

def get_mult_five_first_number(n: int, m: int) -> tuple:
    if abs(n) > abs(m):
        return n * 5, m
    return n, m


if __name__ == '__main__':
    N, M = (int(i) for i in input().split())
    print(*get_mult_five_first_number(N, M))