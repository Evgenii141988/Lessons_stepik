# Даны два натуральных числа A и B. Требуется найти их наибольший общий делитель (НОД) методом вычитания

def get_nod(a, b):
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    return a


if __name__ == '__main__':
    a, b = [int(i) for i in input().split()]
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    print(a)
