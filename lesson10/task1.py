# 1. Реализовать класс Matrix (матрица).
# Конструктор класса __init__() должен принимать список списков чисел для задания превоначального состояния матрицы.
# Подсказка: матрица — это таблица размером N строк на M столбцов (размерность N x M).
# Примеры матриц: 3 на 2, 3 на 3, 2 на 4.
#
# | 31 22 |
# | 37 43 |
# | 51 86 |
#
# | 3 5 32 |
# | 2 4 6 |
# | -1 64 -8 |
#
# | 3 5 8 3 |
# | 8 3 7 1 |
# В методе __init__() надо проверить корректность передаваемых данных - все списки должны быть одинаковой длины.
# В случае расхождения выбрасывать исключение ValueError с соответствующим описанием.
# Добавить метод __add__() сложения двух матриц. Складывать можно матрицы одинаковой размерности.
# В случае, когда пользователь пытается сложить матрицы разных размеров выбросить исключение ValueError.
# В результате сложения двух матриц должна образоваться новая матрица размером N x M, где каждый элемент в ячейке i,j
# образован сложением значений из соответствующих ячеек исходных матриц.
# Реализовть метод __str__(), возвращающий строку вида " 1 2 3\n 4 5 6", отводя под числа по три разряда,
# чтобы для небольших чисел матрица выглядела как таблица.
# Создать три матрицы (две одинаковые по размеру и одну с другим размером).
# Сложить одинаковые матрицы и потом сложить разные. Напечатать исходные таблицы и результат сложения.


class Matrix:

    def __init__(self, list_of_line):
        len_list = len(list_of_line)
        i = 0
        k = 1
        while k < len_list:
            len_line = len(list_of_line[i])
            len_line_next = len(list_of_line[k])
            if len_line != len_line_next:
                raise ValueError('Матрица должна иметь строки одной размерности')
            i += 1
            k += 1
        self.list_of_line = list_of_line

    def size(self):
        size_matrix = len(self.list_of_line)
        size_line = len(self.list_of_line[0])
        return size_matrix, size_line

    def __add__(self, other):
        if self.size() != other.size():
            raise ValueError('Матрицы должны иметь один размер')
        result_list = []
        for i in range(len(self.list_of_line)):
            result_line = []
            for j in range(len(self.list_of_line[i])):
                result_line.append(self.list_of_line[i][j] + other.list_of_line[i][j])
            result_list.append(result_line)
        return Matrix(result_list)

    def __str__(self):
        return '\n'.join(' '.join(f'{i:03}' for i in line) for line in self.list_of_line)


m1 = Matrix([[1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3]])
m2 = Matrix([[4, 5, 6], [4, 5, 6], [4, 5, 6], [4, 5, 6]])
m3 = Matrix([[1, 2, 3], [1, 2, 3], [1, 2, 3]])
m4 = m1 + m2
print(m1)
print('m1----------------->')
print(m2)
print('m2----------------->')
print(m3)
print('m3----------------->')
print(m4)
print('m4----------------->')
m5 = m1 + m3
print(m5)
