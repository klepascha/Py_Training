"""
Напишите программу, которая спрашивает у пользователя два числа и знак: "+" или "-".
В зависимости от знака выводит их сумму или разницу
"""

num_1 = float(input('Enter the first number '))
num_2 = float(input('Enter the second number '))
action = str(input('Enter a sign "+" or "-" '))

if action == '+':
    print('The sum of the numbers is {}'.format(num_1 + num_2))
elif action == '-':
    print('The difference of the numbers is {}'.format(num_1 - num_2))
else:
    print('You have entered an incorrect action')
