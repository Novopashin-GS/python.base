# 5. Реализуйте базовый класс Car.
# при создании класса должны быть переданы атрибуты: color (str), name (str).
# реализовать в классе методы: go(speed), stop(), turn(direction), которые должны изменять состояние машины - для
# хранения этих свойств вам понадобятся дополнительные атрибуты - придумайте какие.
# добавьте метод is_police() - который возвращает True/False, в зависимости от того является ли этот автомобиль
# полицейским (см.дальше)
# Сделайте несколько производных классов: TownCar, SportCar, WorkCar, PoliceCar;
# Добавьте в базовый класс метод get_status(), который должен возвращать в виде строки название, цвет, текущую
# скорость автомобиля и направление движения (в случае если автомобиль едет), для полицейских автомобилей перед
# названием автомобиля должно идти слово POLICE;
# Для классов TownCar и WorkCar в методе get_status() рядом со значением скорости должна выводиться фраза "ПРЕВЫШЕНИЕ!",
# если скорость превышает 60 (TownCar) и 40 (WorkCar).
# Создайте по одному экземпляру каждого производного класса. В цикле из 10 итераций, для каждого автомобиля сделайте
# одно из случайных действий: go, stop, turn со случайными параметрами. После каждого действия показывайте статус
# автомобиля.

import random


class Car:
    speed = random.randint(0, 100)
    direction = ['north', 'south', 'east', 'west']
    current_direction = random.choice(direction)

    def __init__(self, color, name):
        self.color = color
        self.name = name

    def go(self, speed):
        self.speed = speed

    def stop(self):
        self.speed = 0

    def turn(self, direction):
        self.current_direction = direction

    def is_police(self):
        return None

    def get_status(self):
        if self.speed > 0:
            return f'{self.color} {self.name} {self.speed} {self.current_direction}'
        else:
            return f'{self.color} {self.name} {self.speed}'


class TownCar(Car):
    speed_limit = 60

    def get_status(self):
        excess_limit = "ПРЕВЫШЕНИЕ!" if self.speed > self.speed_limit else ""
        if self.speed > 0:
            return f'{self.color} {excess_limit} {self.name} {self.speed} {self.current_direction}'
        else:
            return f'{self.color} {self.name} {self.speed}'


class SportCar(Car):
    pass


class WorkCar(Car):
    speed_limit = 40

    def get_status(self):
        excess_limit = " ПРЕВЫШЕНИЕ!" if self.speed > self.speed_limit else ""
        if self.speed > 0:
            return f'{self.color} {self.name}{excess_limit} {self.speed} {self.current_direction}'
        else:
            return f'{self.color} {self.name} {self.speed}'


class PoliceCar(Car):

    def is_police(self):
        return True

    def get_status(self):
        if self.speed > 0:
            return f'{self.color} POLICE {self.name} {self.speed} {self.current_direction}'
        else:
            return f'{self.color} POLICE {self.name} {self.speed}'


cars = [Car('черная', 'Mazda'), TownCar('белый', 'Porsche'), SportCar('желтый', 'Lamborghini'), WorkCar('зеленый',
        'Ford'), PoliceCar('синий', 'Mercedes-Benz')]

for car in cars:
    for iteration in range(10):
        do = random.randint(1, 3)
        if do == 1:
            car.go(random.randint(1, 100))
        elif do == 2:
            car.stop()
        else:
            car.turn(random.choice(['north', 'south', 'east', 'west']))
        print(car.get_status())
