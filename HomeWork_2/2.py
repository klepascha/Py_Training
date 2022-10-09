# Создать лист из 6 любых чисел. Отсортировать его по возрастанию

print('Exercise 2.1')

new_list = [4, 2, 1, 6, 7, 4, ]
new_list.sort()
print(new_list)

# Создать словарь из 5 пар: int -> str, например {6: '6'}, вывести его в консоль попарно

print('\nExercise 2.2')

new_dict = {5: '5', 3: '3', 1: '1', 6: '6', 7: '7', }
for key, value in new_dict.items():
    print(key, value)

# Создать tuple из 10 любых дробных чисел, найти максимальное и минимальное значение в нем

print('\nExercise 2.3')

new_tuple = (5.2, 2.1, 63.1, 64.2, 162.1, 82.1, 13.3, 21.5, 14.221, 14.2, )
print('The max value is {}, the min value is {}'.format(max(new_tuple), min(new_tuple)))

# Создать лист из 3 слов: ['Earth', 'Russia', 'Moscow'], соеденить все слова в единую строку,
# чтобы получилось: 'Earth -> Russia -> Moscow'

print('\nExercise 2.4')

list_new = ['Earth', 'Russia', 'Moscow', ]
join_string = ' -> '.join(list_new)
print(join_string)

# Взять строку '/bin:/usr/bin:/usr/local/bin' и разбить ее в список по символу ':'

print('\nExercise 2.5')

new_string = '/bin:/usr/bin:/usr/local/bin'
split_string = new_string.split(':')
print(split_string)

# Пройти по всем числам от 1 до 100, написать в консоль, какие из них делятся на 7, а какие - нет

print('\nExercise 2.6')

div_seven = list()
not_div_seven = list()

for num in range(1, 100):
    if num % 7 == 0:
        div_seven.append(num)
    else:
        not_div_seven.append(num)
print('The numbers divisible by seven - {}\nThe numbers not divisible by seven - {}'.format(div_seven, not_div_seven))

# Создать матрицу любых чисел 3 на 4, сначала вывести все строки, потом все столбцы

print('\nExercise 2.7')

matrix = [
    [1, 2, 3, ],
    [4, 5, 6, ],
    [7, 8, 8, ],
    [10, 11, 12],
]

# for i in matrix:
#    print(i)

for i in range(len(matrix)):
    for k in range(len(matrix[i])):
        print(matrix[i][k], end=' ')
    print()

k = 0
for i in range(len(matrix[k])):
    print()
    for k in range(len(matrix)):
        print(matrix[k][i], end=' ')

# Создать список любых объектов, в цикле напечатать в консоль: объект и его индекс

print('\n\nExercise 2.8')

any_list = [None, True, 5, 'str', 5.2]
for i in any_list:
    print(i, any_list.index(i))

# Создать список с тремя значениями 'to-delete' и нескольми любыми другими, удалить из него все значения 'to-delete'

print('\nExercise 2.9')

delete_list = ['to-delete', 'to-delete', 5, 2342, None, 'to-delete', 'str']
while 'to-delete' in delete_list:
    delete_list.remove('to-delete')
print(delete_list)

# Пройти по всем числам от 1 до 10 в обратную сторону (то есть: от 10 до 1), напечатать их в консоль

print('\nExercise 2.10')

print(list(x for x in range(10, 0, -1)))

for num in range(10, 0, -1):
    print(num)
