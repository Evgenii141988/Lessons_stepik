#        Сортировка подсчетом
# Как видно из названия задачи, вам необходимо отсортировать список, состоящий только из чисел в пределах от -100 до 100
# включительно, сортировкой подсчетом.
# Программа получает на вход число n - количество элементов в списке, затем сами элементы списка
# Вам необходимо вывести отсортированный список
# P.S. не пользуйтесь встроенной функцией sorted или методом sort
def get_sort_list(nums: str) -> list:
    numbers = [int(i) for i in nums.split()]
    sort_numbers = [0] * 201
    result = []
    for num in numbers:
        sort_numbers[num + 100] += 1
    for i, elem in enumerate(sort_numbers):
        if elem > 0:
            for _ in range(elem):
                result.append(i - 100)
    return result


if __name__ == '__main__':
    assert get_sort_list('8 9 8 7 2') == [2, 7, 8, 8, 9]
    assert get_sort_list('-8 5 -7 4 -8 0 4') == [-8, -8, -7, 0, 4, 4, 5]
    assert get_sort_list('66 -66 -48 -96 -17 -80 -57 -45') == [-96, -80, -66, -57, -48, -45, -17, 66]

