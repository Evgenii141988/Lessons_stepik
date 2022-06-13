# Напишите программу, которая получает на вход целое десятичное число и осуществляет
# перевод этого числа в шестнадцатеричную строку.

def get_hex_string(n: int) -> str:
    return f"'{hex(n)}'"


if __name__ == '__main__':
    number = int(input())
    print(get_hex_string(number))