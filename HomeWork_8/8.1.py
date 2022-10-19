
import random

# Написать генератор, который бы каждый раз возвращал новое случайное значение
print('gen1')


def gen1():
    while True:
        rand = random.randint(1, 100)
        yield rand


x = gen1()
print(next(x))
print(next(x))

# Написать генератор, который бы работал как renge()
print('gen2')


def gen2(start: int, stop: int, step=1):
    num = start
    while True:
        if num <= stop:
            yield num
            num += step
        else:
            raise StopIteration


x = gen2(2, 6, 2)

print(next(x))
print(next(x))
print(next(x))


# Написать генератор, который бы работал как map()
print('gen3')


def gen3(funk, user_list):
    for i in user_list:
        yield funk(i)


def test(some):
    return some + 1


x = gen3(test, [1, 2, 3, ])

print(next(x))
print(next(x))
print(next(x))


# Написать генератор, который бы работал как enumerate()
print('gen4')


def gen4(user_list):
    count = 0
    for i in user_list:
        yield count, i
        count += 1


x = gen4([1, 2, 3, ])

print(next(x))
print(next(x))
print(next(x))

# Написать генератор, который бы работал как zip()
print('gen5')


def gen5(list1, list2):
    count = len(list1)
    for i in range(count):
        yield list1[i], list2[i]


x = gen5([1, 2, 3, ], [3, 4, 5, ])

print(next(x))
print(next(x))
print(next(x))
