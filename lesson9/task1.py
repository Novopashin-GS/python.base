# 1. Создать класс TrafficLight (светофор).
# определить у него один приватный атрибут color (цвет) и метод get_current_signal() (получить текущий цвет);
# после создания экземпляра светофора, он запускает режим смены сигналов с разной длительностью: красный (3 сек),
# жёлтый (1 сек), зелёный (3 сек);
# переключение идет циклично в порядке красный-жетлый-зеленый-красный-жетлый-зеленый-красный-...
# проверить переключение режимов работы светофора, опрашивая в цикле текущее состояние светофора с интервалом 0.5
# секунды, используя метод get_current_signal().


from datetime import datetime
from time import sleep


class TrafficLight:
    __color = 'None'
    __time_of_color = [3, 1, 3]
    time_of_cycle = sum(__time_of_color)

    def __init__(self):
        self.start = datetime.now()

    def get_current_signal(self):
        current_seconds = (datetime.now() - self.start).total_seconds()
        if current_seconds % self.time_of_cycle <= self.__time_of_color[0]:
            self.__color = 'red'
        elif current_seconds % self.time_of_cycle <= self.__time_of_color[0] + self.__time_of_color[1]:
            self.__color = 'yellow'
        else:
            self.__color = 'green'
        return self.__color


light = TrafficLight()
for i in range(30):
    print(datetime.time(datetime.now()), light.get_current_signal())
    sleep(0.5)
