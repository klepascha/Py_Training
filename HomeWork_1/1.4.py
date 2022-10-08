"""
Напишите программу, которая выводит все кратные 5 числа между двумя пользовательскими числами
"""

num_1 = int(input('Enter the first natural integer '))
num_2 = int(input('Enter the second natural integer '))

for num in range(num_1, num_2):
    if num % 5 == 0:
        print(num)
