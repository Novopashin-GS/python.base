# 2. Реализовать проект расчёта суммарного расхода ткани на производство одежды.
# Создать абстрактный класс Clothes (одежда). Сделать в этом классе свойство cloth_size
# (используя декоратор @property) - размер ткани, необходимый для производства одежды.
# Это свойство должно вычислять размерт ткани, вызывая абстрактный метод self.get_size().
# Сделать два производных класса одежды: Suit (костюм) и Coat (Пальто).
# В конструктор Suit должен принимать параметр height (рост), а Coat - size (размер).
# Для определения расхода ткани по каждому типу одежды внутри метода get_size() использовать формулы:
#
# для пальто: (size/6.5 + 0.5)
# для костюма: (2*height + 0.3)
# Создать список из 10 единиц одежды случайно выбирая один из двух возможных типов со случайным параметром.
# Распечатать список одежды: размер требуемой ткани, тип и параметр.
# Рассчитать и вывести на экран общий объем ткани, необходимый для пошива всей одежды из этого списка,
# используя свойство cloth_size. Например:
#
# 30.3 - Suit (height: 15)
# 20 - Coat (size: 3)
# 13.5 - Coat (size: 2)
# 4.3 - Suit (size: 2)
# ...
# Итого: 250.3
import random
from abc import ABC, abstractmethod


class Clothes(ABC):

    @property
    def cloth_size(self):
        return self.get_size()

    @abstractmethod
    def get_size(self):
        pass


class Suit(Clothes):

    def __init__(self, height):
        self.height = height

    def get_size(self):
        return round(2 * self.height + 0.3)


class Coat(Clothes):

    def __init__(self, size):
        self.size = size

    def get_size(self):
        return round(self.size/6.5 + 0.5)


clothes = []
for i in range(10):
    number = random.randint(1, 100)
    if number > 50:
        clothes.append(Suit(random.randint(1, 200)))
    else:
        clothes.append(Coat(random.randint(1, 200)))
all_sum = 0
for i in clothes:
    print(i.cloth_size, type(i), i.__dict__)
    all_sum += i.cloth_size
print(all_sum)
