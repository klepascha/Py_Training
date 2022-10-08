"""
Напишите программу, которая находит все простые числа между 0 и пользовательским числом
"""

num = int(input('Enter a natural integer not equal to zero or one '))

if num <= 1:
    print('Your number does not meet the specified conditions')
else:
    for nummer in range(2, num + 1):
        k = 0
        for i in range(2, nummer // 2 + 1):
            if nummer % i == 0:
                k += 1
        if k <= 0:
            print(nummer)
