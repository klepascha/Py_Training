"""
Написать декоратор, который отменяет выполнение любой декорированной функций и будет писать в консоль: ИМЯ_ФУНКЦИИ is canceled!
Реализовать декоратор, который измеряет скорость выполнения функций.
Реализовать декоратор, который будет считать, сколько раз выполнялась функция
Реализовать декоратор, который будет логгировать процесс выполнения функции: создан декоратор, начато выполнение функции, закончено выполнение функции
Реализовать декоратор, который будет перехватывать все исключения в функции. Если они случились, нужно просто писать в консоль сообщение об ошибке
"""

from time import time


def cancel_function(function):
    def inner():
        print('{} is canceled!'.format(function.__name__))
    return inner


def speed_function(function):
    def inner():
        start_time = time()
        function()
        end_time = time()
        print('Func was {} long'.format(end_time - start_time))
    return inner


class Counter(object):
    counts = {}
    @staticmethod
    def count(function):
        def inner():
            function()
            if function.__name__ in Counter.counts.keys():
                Counter.counts[function.__name__] += 1
                print(Counter.counts[function.__name__])
            else:
                Counter.counts[function.__name__] = 1
                print(Counter.counts[function.__name__])
        return inner


def logger(function):
    def inner():
        print('Dec has been created')
        print('func has beem started')
        function()
        print('Func has been finished')
    return inner


def catcher(function):
    def inner():
        try:
            function()
        except Exception as e:
            print(e)
    return inner


@cancel_function
def some_func():
    print("I'm some func")


@speed_function
def some_func2():
    print("I'm some func")


@Counter.count
def some_func3():
    print("I'm some func")


@Counter.count
def some_func4():
    print("I'm some func")


@logger
def some_func5():
    print("I'm some func")


@catcher
def some_func6():
    print(5/0)


def main():
    some_func()
    some_func2()
    some_func3()
    some_func3()
    some_func3()
    some_func4()
    print(Counter.counts)
    some_func5()
    some_func6()


if __name__ == '__main__':
    main()
