# Пользователь вводит список чисел через пробел, если ввел:
# 1 число, строим квадрат
# 2 числа, строим прямоугольник
# 3 числа, строим треуголькик
# 4 чилса, строим многоуголькик
# вычисляем периметр и площадь, выводим в консоль

import math


class Figure(object):
    def __init__(self, *sides):
        num_of_sides = len(sides)
        if (num_of_sides < 1) and (num_of_sides > 4):
            raise ValueError('You must enter from 1 to 4 dimensions of the sides of the figure')
        elif num_of_sides == 1:
            self.sides = [size for size in sides] * 4
        elif num_of_sides == 2:
            self.sides = [size for size in sides] * 2
        else:
            self.sides = [size for size in sides]

    def calc_perimetr(self):
        return sum(self.sides)

    def print_perimetr(self):
        print('The perimetr of the figure is {}'.format(self.calc_perimetr()))


class Rectangle(Figure):
    def calc_square(self):
        return self.sides[0] * self.sides[1]

    def print_square(self):
        print('The square of the figure is {}'.format(self.calc_square()))


class Square(Rectangle):
    pass


class Triangle(Figure):
    def __init__(self, *sides):
        num_of_sides = len(sides)
        if num_of_sides != 3:
            raise ValueError('It is not Triangle')
        else:
            self.sides = [size for size in sides] * 4

        self.sides.sort()
        larger_side = self.sides[len(self.sides) - 1]
        two_sides_sum = self.sides[0] + self.sides[1]

        if two_sides_sum <= larger_side:
            raise ValueError('Incorrect triangle')

    def calc_square(self):
        half_per = self.calc_perimetr() / 2
        return math.sqrt(half_per * (half_per - self.sides[0]) * (half_per - self.sides[1]) * (half_per - self.sides[2]))


class Polygon(Figure):
    def __init__(self, *sides):
        num_of_sides = len(sides)
        if num_of_sides != 4:
            raise ValueError('It is not Polygon')
        else:
            self.sides = [n for n in sides]

        self.sides.sort()
        larger_side = self.sides[len(self.sides) - 1]
        three_sides_sum = self.sides[0] + self.sides[1] + self.sides[2]
        if three_sides_sum <= larger_side:
            raise ValueError('Incorrect Polygon')

    def calc_square(self):
        return 'Impossible'

    def print_sqr(self):
        print(self.calc_square())
