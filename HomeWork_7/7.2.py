"""
При помощи map посчитать остаток от деления на 5 для чисел: [1, 4, 5, 30, 99]
При помощи map превратить все числа из массива [3, 4, 90, -2] в строки
При помощи filter убрать из массива ['some', 1, 'v', 40, '3a', str] все строки
При помощи reduce посчитать количество букв в словах: ['some', 'other', 'value']
"""

from functools import reduce

first = list(map(lambda x: x % 5, [1, 4, 5, 30, 99]))
second = list(map(lambda x: str(x), [3, 4, 90, -2]))
third = list(filter(lambda x: type(x) is not str, ['some', 1, 'v', 40, '3a', str]))
fourth = reduce(lambda x, y: x + y, list(len(z) for z in ['some', 'other', 'value']))

print(first)
print(second)
print(third)
print(fourth)
