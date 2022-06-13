# Напишите программу, которая получает на вход целое десятичное
# число и осуществляет перевод этого числа в восьмеричную систему счисления.

def get_oct_number(n: int) -> int:
    return int(f'{n: o}')


if __name__ == '__main__':
    numbers = int(input())
    print(get_oct_number(numbers))
