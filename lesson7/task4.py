#  Написать скрипт, который выводит статистику для заданной папки в виде словаря, в котором ключи — верхняя граница
#  размера файла (пусть будет кратна 10), а значения — общее количество файлов (в том числе и в подпапках),
#  размер которых не превышает этой границы, но больше предыдущей (начинаем с 0), например:
#     {
#       100: 15,
#       1000: 3,
#       10000: 7,
#       100000: 2
#     }
# Тут 15 файлов размером не более 100 байт; 3 файла больше 100 и не больше 1000 байт...
# Подсказка: размер файла можно получить из атрибута .st_size объекта os.stat.


import os
my_dict = {}
count_of_size_hundred = 0
count_of_size_thousand = 0
count_of_size_ten_thousand = 0
for cdir, subdirs, files in os.walk('..'):
    for file in files:
        size = os.stat(os.path.join(cdir, file)).st_size
        if size < 100:
            count_of_size_hundred += 1
        elif size < 1000:
            count_of_size_thousand += 1
        elif size < 10000:
            count_of_size_ten_thousand += 1
my_dict.setdefault(100, count_of_size_hundred)
my_dict.setdefault(1000, count_of_size_thousand)
my_dict.setdefault(10000, count_of_size_ten_thousand)
print(my_dict)
