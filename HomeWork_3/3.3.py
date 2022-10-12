"""
Написать функцию, которая принимает любое количество аргументов чисел. Среди них она находит максимальное и минимальное.
И возвращает оба
"""


def max_min(*numbers):
    max_number = max(numbers)
    min_number = min(numbers)
    return max_number, min_number


print(max_min(1, 3, 5, 6, 7, 8))

"""
Написать функцию, которая принимает два аргумента: строка и булевый флаг case по-умолчанию равный True. 
Если флаг действителен: возвращаем новую строку, где каждый символ входной приведен к верхнему регистру, иначе - 
к нижнему
"""


def case_func(user_string: str, case: bool = True):
    if case:
        return user_string.upper()
    else:
        return user_string.lower()


print(case_func('MyaW'), case_func('MyaW', case=False))

"""
Написать функцию, которая принимает любое количество позиционных аргументов - строк и один парматер по-умолчанию glue, 
который равен ':'. Соединить все строки таким образом, чтобы в результат попали все строки, длинее 3 символов. 
Для соединения между любых двух строк вставлять glue
"""


def glue_func(*user_string: str, glue=':'):
    new_string = list(user_string)
    print(new_string)
    for string in new_string:
        if len(string) < 3:
            new_string.remove(string)
    result = glue.join(new_string)
    return result


print(glue_func('qwer', 'as', 'zxcva', 'Maksim', glue='*'))
