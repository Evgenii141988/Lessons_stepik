# Даны два натуральных числа A и B. Требуется найти их наибольший общий делитель (НОД) методом вычитания

a, b = [int(i) for i in input().split()]
while a != b:
    if a > b:
        a -= b
    else:
        b -= a
print(a)