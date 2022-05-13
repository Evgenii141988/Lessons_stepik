#        Сортировка подсчетом
# Как видно из названия задачи, вам необходимо отсортировать список, состоящий только из чисел в пределах от -100 до 100
# включительно, сортировкой подсчетом.
# Программа получает на вход число n - количество элементов в списке, затем сами элементы списка
# Вам необходимо вывести отсортированный список
# P.S. не пользуйтесь встроенной функцией sorted или методом sort

n = int(input())
numbers = [int(i) for i in input().split()]
sort_numbers = [0] * 201
for num in numbers:
    sort_numbers[num + 100] += 1
# print(sort_numbers)
for i in range(len(sort_numbers)):
    if sort_numbers[i] > 0:
        for _ in range(sort_numbers[i]):
            print(i - 100, end=' ')
