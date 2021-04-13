# 2. Реализовать класс Road (дорога).
# определить защищенные атрибуты: length (длина), width (ширина);
# значения атрибутов должны передаваться при создании экземпляра класса;
# определить внутри класса приватную константу масса квадратного метра асфальта толщиной 1 см.
# определить метод расчёта массы асфальта get_asphalt_mass(height), необходимого для покрытия всей дороги толщиной
# height см;
# использовать формулу: длина * ширина * масса асфальта для покрытия одного кв. метра дороги асфальтом, толщиной в
# 1 см * число см толщины полотна;
# проверить работу метода.
# Например: 20 м*5000 м*25 кг*5 см = 12500 т.


class Road:
    __weight_per_square_meter_of_asphalt = 1

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def get_asphalt_mass(self, height):
        return f'{self._width * self._length * self.__weight_per_square_meter_of_asphalt * height/1000} т.'


road = Road(20, 500)
print(road.get_asphalt_mass(25))

