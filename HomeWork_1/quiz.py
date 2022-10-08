"""
Программа выводить в консоль текст загадки и ждать ввода пользователя
Программа после ввода пользователя ответа должна вывести в консоль результат: правильный ли ответ дал пользователь
Программа должна в конце игры сказать, сколько ответов дал пользователь: сколько из них было верных
Программа должна не учитывать регистр ответа
"""

# Creating a dictionary of questions and answers
dict_quiz = {
    'Какой знак показывает остаток от деления ': '%',
    'Какой тип данных соответствует числу "5" ': 'int',
    'Какой тип данных соответствует числу "2,5" ': 'float',
    'Какой тип данных соответствует текстовым срокам ': 'str',
    'Как на языке Python обозначается "истина" ': 'true',
    'Как на языке Python обозначается "ложь" ': 'false',
    'Как на языке Python обозначается цикл с предусловием ': 'while',
    'Как на языке Python обозначается перебирающий цикл ': 'for',
    'Какой знак используют для целочисленного деления ': '//',
    'Какой знак используют для возведения в степень числа ': '**'
}
# Сounter initiation
counter_answer_right = [0, 0]

for question in dict_quiz:
    answer = input(question)
    if answer.lower() == dict_quiz.get(question).lower():
        print('Great!')
        counter_answer_right[0] += 1
        counter_answer_right[1] += 1
    elif not answer.lower() :
        print('You missed the question :С')
    else:
        print('Incorrect')
        counter_answer_right[0] += 1

print('Вы ответили на {} вопросов из 10, из них верными оказалось {}'.format(counter_answer_right[0],
                                                                             counter_answer_right[1]))
