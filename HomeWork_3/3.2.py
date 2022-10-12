"""
Написать функцию, которая принимает на вход два аргумента. Если аргументы больше нуля, возвращаем их сумму. Если оба
меньше - разность. Если знаки разные - возвращаем 0
"""


def func_1(arg_1, arg_2):
    if arg_1 > 0 and arg_2 > 0:
        return arg_1 + arg_2
    elif arg_1 < 0 and arg_2 < 0:
        return arg_1 - arg_2
    elif (arg_1 * arg_2) < 0:
        return 0


print(func_1(2, 4), func_1(-2, -5), func_1(5, -2))

"""
Написать функцию, которая принимает 3 аргумента - числа, найти среди них два максимальных, вывести в консоль
"""


def func_2(num1, num2, num3):
    num_list = [num1, num2, num3]
    num_list.sort()
    return num_list[1], num_list[2]


print(func_2(1, 5, 3))

"""
Написать функцию, которая принимает два аргумента. Первый - список чисел, второй - булевый флаг. Если флаг действителен 
- возвращаем новый список с нечетными числами из входного списка, если флаг отрицателен - возвращаем новый список с 
четными числами из входного списка
"""


def func_3(numbers: list, flag: bool):
    result = list()
    if flag:
        for num in numbers:
            if num % 2 == 0:
                result.append(num)
    else:
        for num in numbers:
            if num % 2 != 0:
                result.append(num)
    return result


print(func_3([1, 3, 5, 3, 8, 3, 12, 4], True), func_3([2, 5, 7, 8, 3, 1, 9], False))