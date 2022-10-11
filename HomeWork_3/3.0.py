
import random

"""
Написать фугкцтю, которая выпрасывает одно из трех исключений: ValueError, TypeError млм RuntimeError случайным
образом. В месте вызова функции обрабатывается все три исключения.
"""


def raise_random():
    random_number = random.randint(1, 3)
    if random_number == 1:
        raise ValueError('ValueError')
    elif random_number == 2:
        raise TypeError('TypeError')
    else:
        raise RuntimeError('RuntimeError')


try:
    raise_random()
except ValueError as err:
    print('Error - ', err)
except TypeError as err:
    print('Error - ', err)
except RuntimeError as err:
    print('Error - ', err)

"""
Написать функцию, которая принимает на вход список, если в списке все объекты - itn, сортирует его. Иначе выбрасывает 
ValueError
"""


def sort_int(*numbers):
    if not any(not isinstance(num, int) for num in numbers):
        sort_list = list(numbers)
        sort_list.sort()
        return sort_list
    else:
        raise ValueError('Not integer figures')


"""
Написать функцию, которая принимает словарь, преобразует все ключи словаря к строкам и возвращает новый результат.
"""


def str_dict(user_dict):
    new_dict = {}
    for key, value in user_dict.items():
        new_dict.update({str(key): value})
    return new_dict


"""
Написать функцию, которая принимает список чисел и возвращает их произведение
"""


def multi_number(*numbers):
    multi_result = 1
    for num in numbers:
        multi_result *= num
    return multi_result
