# Программа получает на вход натуральное число N.
# Нужно найти сумму его делителей.
def get_sum_del(n: int) -> int:
    total = 0
    i = 1
    while i * i <= n:
        if n % i == 0:
            total += i
            if total == n == 1:
                break
            if i != n // 2:
                total += n // i
        i += 1
    return total


if __name__ == '__main__':
    n = int(input())
    print(get_sum_del(n))