#                  Слияние списков
# В вашем распоряжении имеется два отсортированных списка по неубыванию элементов, состоящих из n и m элементов
# Ваша задача слить их в один отсортированный список размером  n + m
# Входные данные
# Программа получает на вход два числа n и m - количество элементов первого списка и второго списков
# Затем с новой строки поступают элементы первого отсортированного списка, а со следующей строки - второго списка
# Выходные данные
# Слить два списка в один в порядке неубывания и вывести элементы полученного списка
# P.S: пользоваться встроенной сортировкой запрещено
# Примечание: для вывода результирующего списка вы можете использовать следующую конструкцию
# print(*result) # где result - итоговый список
def merge_two_sotr_list(list1: list, list2: list) -> list:
    result = []
    p1 = 0
    p2 = 0
    while p1 < n and p2 < m:
        if list1[p1] <= list2[p2]:
            result.append(list1[p1])
            p1 += 1
        else:
            result.append(list2[p2])
            p2 += 1
    if p1 < len(list1):
        result += list1[p1:]
    if p2 < len(list2):
        result += list2[p2:]
    return result

if __name__ == '__main__':
    n, m = map(int, input().split())
    list1 = [int(i) for i in input().split()]
    list2 = [int(i) for i in input().split()]
    result = []
    p1 = 0
    p2 = 0
    while p1 < n and p2 < m:
        if list1[p1] <= list2[p2]:
            result.append(list1[p1])
            p1 += 1
        else:
            result.append(list2[p2])
            p2 += 1
    if p1 < len(list1):
        result += list1[p1:]

    if p2 < len(list2):
        result += list2[p2:]
    print(*result)
    print(*merge_two_sotr_list(list1, list2))

