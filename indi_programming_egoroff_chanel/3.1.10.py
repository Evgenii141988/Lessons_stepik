# Для положительного целого числа n определим функцию f:
# f(n)=-1+2-3+..+(-1)nn
# Ваша задача — посчитать f(n) для данного целого числа n.
# В единственной строке записано положительное целое число n (1≤n≤10 ** 15).
# Выведите f(n) в единственной строке.
# Примечание
# f(4)=-1+2-3+4=2
# f(5)=-1+2-3+4-5=-3

n = int(input())
if n % 2 == 0:
    print(n // 2)
else:
    print(n // (-2))