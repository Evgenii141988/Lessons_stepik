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


def get_index_num(numbers: list) -> int:
    return numbers.index(get_largest_simple_num(numbers))


def get_sum_digits(num: int) -> int:
    num_str = str(num)
    digits = [int(i) for i in num_str]
    return sum(digits)


if __name__ == '__main__':
    numbers = [int(i) for i in input().split()]
    number = get_largest_simple_num(numbers)
    print(get_index_num(numbers), get_sum_digits(number))
