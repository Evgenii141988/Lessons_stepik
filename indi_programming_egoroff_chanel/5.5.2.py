#                 Постулат Бертрана
# Постулат Бертрана (теорема Бертрана-Чебышева, теорема Чебышева) гласит, что для любого n > 1 найдется простое число
# p в интервале n < p < 2n. Такая гипотеза была выдвинута в 1845 году французским математиком Джозефем Бертраном
# (проверившим ее до n=3000000) и доказана в 1850 году Пафнутием Чебышевым. Рамануджан в 1920 году нашел более
# простое доказательство, а Эрдеш в 1932 – еще более простое.
# Ваша задача состоит в том, чтобы решить несколько более общую задачу – а именно по числу n найти количество
# простых чисел p из интервала n < p < 2n.
# Напомним, что число называется простым, если оно делится только само на себя и на единицу.
# Входные данные
# Программа принимает на вход целое число n (2 ≤ n ≤ 50000).
# Выходные данные
# Вам необходимо вывести на экран одно число – количество простых чисел p на интервале  n < p < 2n.
def count_simple_num(n):
    count = 0
    index = 0
    for i in range(n + 1, 2 * n):
        if i % 2 == 0:
            continue
        for j in range(3, int(i ** 0.5) + 1, 2):
            if i % j == 0:
                index += 1
                break
        if index > 0:
            index = 0
        else:
            count += 1
    return count

if __name__ == '__main__':
    assert count_simple_num(2) == 1
    assert count_simple_num(4) == 2
    assert count_simple_num(7) == 2
    assert count_simple_num(11) == 3