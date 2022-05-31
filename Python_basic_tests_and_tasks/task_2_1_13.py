# На вход программе подается список целых чисел, разделённых через пробел.
# Напишите программу, которая найдет среди них м
# и выведет на экран индекс числа в списке и через пробел сумму его цифр.

def get_largest_simple_num(numbers: list) -> int:
    largest_simple_num = 0
    for num in numbers:
        counter = 0
        for i in range(2, num // 2 + 1):
            if num % i == 0:
                counter += 1
            if counter == 1:
                break
        if counter == 0 and num > largest_simple_num:
            largest_simple_num = num
    return largest_simple_num


if __name__ == '__main__':
    pass
