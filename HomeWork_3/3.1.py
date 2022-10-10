"""
Пользователь вводит число, если оно четное - выбрасываем исключение ValueError,
если оно меньше 0 - TypeError, если оно больше 10 - IndexError.
Обрабатываем ошибку, говорим пользователю, в чем его ошибка
"""

user_input = int(input('Enter your number '))

try:
    if user_input % 2 == 0:
        raise ValueError('ValueError')
    if user_input < 0:
        raise TypeError('TypeError')
    if user_input > 10:
        raise IndexError('IndexError')
except ValueError as err:
    print('Your error is', err)
except TypeError as err:
    print('Your error is', err)
except IndexError as err:
    print('Your error is', err)


"""
Создайте список произвольной длины. Пользователь должен ввести индекс объекта, который хочет посмотреть. 
Если все хорошо - пишите объект в консоль. Если нет - обработайте возмозможные ошибки и скажите ему, что не так
"""

new_list = list(range(1, 10))
input_user = int(input('Enter your number '))

try:
    print(new_list[input_user])
except Exception as error:
    print(error)
