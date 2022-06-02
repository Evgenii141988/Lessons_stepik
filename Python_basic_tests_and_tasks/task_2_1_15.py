# На вход программе подается список вещественных чисел, разделённых через пробел.
# Напишите программу, которая будет округлять их в сторону следующего целого числа, затем возводить его в квадрат и
# прибавлять к предыдущему, уже возведенному в квадрат числу(см. логику на картинке).
# Вывести на экран получившийся список через пробел.
from math import ceil


def get_round_numbers(nums: list) -> list:
    return [ceil(i) for i in nums]


def get_squad_numbers(nums: list) -> list:
    return [i ** 2 for i in nums]


def get_add_previous_numbers(nums: list) -> list:
    result_numbers = []
    box = 0
    for num in nums:
        result_numbers.append(num + box)
        box += num
    return result_numbers


if __name__ == '__main__':
    numbers = [float(i) for i in input().split()]
