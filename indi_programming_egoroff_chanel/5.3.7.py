#                 Правильная скобочная последовательность
# Наша программа принимает на вход последовательность скобочных символов. Ваша задача определить является
# ли введенная скобочная последовательность правильной.
# Правильная скобочная последовательность (ПСП) называется строка, состоящая только из символов "скобки",
# где каждой закрывающей скобке найдётся соответствующая открывающая (причём того же типа). При этом учитывайте, что:
# Пустая последовательность является правильной.
# Если A – правильная скобочная последовательность, то (A), [A] и {A} – правильные скобочные последовательности.
# Если A и B – правильные скобочные последовательности, то AB – правильная скобочная последовательность.
# Если введенная строка является ПСП, выведите YES, в противном случае - NO.
def check_correct_bracket_sequence(string: str) -> str:
    strings = ['()', '{}', '[]']
    new_string = ''
    for s in string:
        new_string += s
        if len(new_string) > 1 and new_string[-2:] in strings:
            new_string = new_string[:-2]
    return ('NO', 'YES')[len(new_string) == 0]

if __name__ == '__main__':
    # string = input()
    assert check_correct_bracket_sequence('[]') == 'YES'
    assert check_correct_bracket_sequence('[(])') == 'NO'
    assert check_correct_bracket_sequence('({[]}())') == 'YES'
    assert check_correct_bracket_sequence('{[{]}(})') == 'NO'
    assert check_correct_bracket_sequence('[](){}') == 'YES'
    assert check_correct_bracket_sequence('{[]}([)]') == 'NO'

