# Программа получает на вход натуральное число N.
# Нужно найти сумму его делителей.
n = int(input())
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
print(total)