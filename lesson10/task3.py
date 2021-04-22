# 3. Осуществить программу работы с органическими клетками, состоящими из ячеек.
# Необходимо создать класс «Клетка». В его конструкторе инициализировать параметр,
# соответствующий количеству ячеек клетки (целое число). В классе должны быть реализованы методы перегрузки
# арифметических операторов: сложение (__add__()), вычитание (__sub__()), умножение (__mul__()), деление
# (__truediv__()).Эти методы должны применяться только к клеткам и выполнять увеличение, уменьшение, умножение и
# округление до целого числа деления клеток, соответственно.
# Сложение. Объединение двух клеток. При этом число ячеек общей клетки должно равняться сумме ячеек исходных двух
# клеток. Вычитание. Участвуют две клетки. Операцию необходимо выполнять, только если разность количества ячеек
# двух клеток больше нуля, иначе выводить соответствующее сообщение.
# Умножение. Создаётся общая клетка из двух. Число ячеек общей клетки — произведение количества ячеек этих двух клеток.
# Деление. Создаётся общая клетка из двух. Число ячеек общей клетки определяется как целочисленное деление количества
# ячеек этих двух клеток.
# Добавить к классу метод print(columns), распечатыващий на экране звездочки рядами по columns звездочек в одном ряду
# в количестве равном числу ячеек клетки.
# Если ячеек на формирование ряда не хватает, то в последний ряд записываются все оставшиеся.
# Например, если в клетке 12 ячеек, а запросили напечатать по 5 звездочек в ряду, то на экране должно быть:
# *****
# *****
# **

class Cell:

    def __init__(self, cell):
        self.cell = cell

    def __add__(self, other):
        return Cell(self.cell + other.cell)

    def __sub__(self, other):
        if other.cell > self.cell:
            raise ValueError('Вычитание должно происходить из большего меньшее')
        return Cell(self.cell - other.cell)

    def __mul__(self, other):
        return Cell(self.cell * other.cell)

    def __truediv__(self, other):
        return Cell(self.cell//other.cell)

    def print(self, columns):
        for i in range(self.cell//columns):
            print('*' * columns)
        if self.cell % columns > 0:
            print('*' * (self.cell % columns))


cell_1 = Cell(12)
cell_2 = Cell(6)
cell_3 = cell_2 + cell_1
cell_4 = cell_1 - cell_2
cell_5 = cell_1 * cell_2
cell_6 = cell_1 / cell_2
print(cell_3.cell)
cell_3.print(5)
print(cell_4.cell)
cell_4.print(2)
print(cell_5.cell)
cell_5.print(12)
print(cell_6.cell)
cell_6.print(2)