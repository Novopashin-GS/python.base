# 5. * (вместо 4) Написать скрипт, который выводит статистику для заданной папки в виде словаря, в котором ключи те же,
# а значения — кортежи вида (<files_quantity>, [<files_extensions_list>]), например:
#   {
#       100: (15, ['txt']),
#       1000: (3, ['py', 'txt']),
#       10000: (7, ['html', 'css']),
#       100000: (2, ['png', 'jpg'])
#     }
# Сохраните результаты в файл <folder_name>_summary.json в той же папке, где запустили скрипт

import os
import json
my_dict = {}
list_with_size_hundred = []
list_with_size_thousand = []
list_with_size_ten_thousand = []
count_with_size_hundred = 0
count_with_size_thousand = 0
count_with_size_ten_thousand = 0
for cdir, subdirs, files in os.walk('..'):
    for file in files:
        size = os.stat(os.path.join(cdir, file)).st_size
        name, extensions = os.path.splitext(file)
        if size < 100:
            count_with_size_hundred += 1
            list_with_size_hundred.append(extensions) if list_with_size_hundred.count(extensions) == 0 else None
        elif size < 1000:
            count_with_size_thousand += 1
            list_with_size_thousand.append(extensions) if list_with_size_thousand.count(extensions) == 0 else None
        elif size < 10000:
            count_with_size_ten_thousand += 1
            list_with_size_ten_thousand.append(extensions) if list_with_size_ten_thousand.count(extensions) == 0\
                else None
my_dict.setdefault(100, (count_with_size_hundred, list_with_size_hundred))
my_dict.setdefault(1000, (count_with_size_thousand, list_with_size_thousand))
my_dict.setdefault(10000, (count_with_size_ten_thousand, list_with_size_ten_thousand))
print(my_dict)
with open('summary.json', 'w', encoding='utf-8') as f:
    json.dump(my_dict, f, indent=4)
