# На вход программе подается список вещественных чисел, разделённых через пробел.
# Напишите программу, которая находит самые ближайшие в списке числа и выводит
# их на экран в порядке возрастания. Они не должны быть равны друг другу.
def get_two_closest_nums(numbers: list) -> tuple:
    numbers.sort()
    a = numbers[0]
    b = numbers[1]
    diff = b - a
    for i in range(1, len(numbers) - 1):
        if 0 < numbers[i + 1] - numbers[i] < diff:
            a, b = numbers[i], numbers[i + 1]
            diff = b - a
    return a, b


if __name__ == '__main__':
    numbers = [float(i) for i in input().split()]
    print(*get_two_closest_nums(numbers))