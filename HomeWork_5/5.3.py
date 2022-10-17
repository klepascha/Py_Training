"""
Реализовать класс Person, у которого должно быть два публичных поля: age и name.
Также у него должен быть следующий набор методов: know(person), который позволяет
добавить другого человека в список знакомых. И метод is_known(person), который возвращает знакомы ли два человека
"""


class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.i_know = []

    def know(self, person):
        self.i_know.append(person)

    def is_know(self, person):
        if person in self.i_know:
            return True
        else:
            return False


"""
Есть класс, который выводит информацию в консоль: Printer, у него есть метод: log(*values).
Написать класс FormattedPrinter, который выводит в консоль информацию, окружая ее строками из *
"""


class Printer(object):
    def log(self, *values):
        print(*values)


class FormattedPrinter(Printer):
    def formatted_log(self, *values):
        print('***********')
        self.log(*values)
        print('***********')


p = Printer()
p.log(1, 2, 3, 4, 5, 6)

p = FormattedPrinter()
p.log(1, 2, 3, 4, 5, 6)
p.formatted_log(1, 2, 3, 4, 5, 6)

"""
Написать класс Animal и Human,сделать так, чтобы некоторые животные были опасны для человека (хищники, ядовитые).
Другие - нет. За что будет отвечать метод is_dangerous(animal)
"""


class Animal(object):
    def __init__(self, danger):
        self.danger = danger

    def is_dangerous(self):
        if self.danger:
            print('This animal is dangerous')
        else:
            print('This Animal is not dangerous')


cat = Animal(False)
tiger = Animal(True)
cat.is_dangerous()
tiger.is_dangerous()
