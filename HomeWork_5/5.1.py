# Создать класс корзина, у которого можо выставлить разнеую вметительность для разных объектов.
# В объекты класса корзина можно помещать разные  объекты.
# Создать класс пакет, в который можно помещать предметы. У него тоже есть вместимость.
# Создать любой класс, объекты которого можно было помещать в корхину и пакет.
# Если вместимости  недостаточно, сказать, что объект поместить нельзя

class Basket(object):
    def __init__(self, capacity):
        self.capacity = capacity
        self.in_basket = []

    def place(self, thin):
        if self.capacity >= thin.weight:
            self.in_basket.append(thin)
            print(self, 'is in')
            self.capacity -= thin.weight
        else:
            print('not enough space ')

    def what_in(self):
        print(self.in_basket)


class Package(Basket):
    pass


class Garbage(object):
    def __init__(self, weight):
        self.weight = weight


bs1 = Basket(10)
pc1 = Package(100)
gb1 = Garbage(500)
gb2 = Garbage(14)
gb3 = Garbage(5)

bs1.place(gb3)
bs1.place(gb3)
bs1.place(gb1)
bs1.what_in()

pc1.place(gb1)
pc1.place(gb2)
pc1.what_in()
