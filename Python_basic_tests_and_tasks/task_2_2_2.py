# На вход подается натуральное четырехзначное число. Напишите программу, которая выводит True,
# если сумма крайних цифр равна сумме средних и False в противном случае.
def get_correct_number(n: int) -> bool:
    n = str(n)
    return int(n[0]) + int(n[-1]) == int(n[1]) + int(n[-2])


if __name__ == '__main__':
    number = int(input())
    print(get_correct_number(number))
