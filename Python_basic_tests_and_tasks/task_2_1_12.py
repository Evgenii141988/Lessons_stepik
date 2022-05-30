# На вход программе подается список целых чисел, разделённых через пробел.
# Напишите программу, которая выводит через пробел самое наибольшее отрицательное
# число и самое наименьшее положительное, либо 0 если какого-либо из них нет.

def get_max_negative_num(numbers: list) -> int:
    negative_nums = [i for i in numbers if i < 0]
    if negative_nums:
        return max(negative_nums)
    return 0


def get_min_positive_num(numbers: list) -> int:
    positive_nums = [i for i in numbers if i > 0]
    if positive_nums:
        return min(positive_nums)
    return 0


if __name__ == '__main__':
    numbers = [int(i) for i in input().split()]
    print(get_max_negative_num(numbers), get_min_positive_num(numbers))
