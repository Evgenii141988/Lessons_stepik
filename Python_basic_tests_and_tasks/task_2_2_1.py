# Напишите программу, которая получает на вход целое десятичное число и осуществляет перевод этого
# числа в двоичную систему счисления.

def get_binary_number(n):
    return int(bin(n)[2:])


if __name__ == '__main__':
    number = int(input())
    print(get_binary_number(number))
