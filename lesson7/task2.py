# 2. * (вместо 1) Написать скрипт, создающий из config.yaml стартер для проекта со следующей структурой:
# |--my_project
#    |--settings
#    |  |--__init__.py
#    |  |--dev.py
#    |  |--prod.py
#    |--mainapp
#    |  |--__init__.py
#    |  |--models.py
#    |  |--views.py
#    |  |--templates
#    |     |--mainapp
#    |        |--base.html
#    |        |--index.html
#    |--authapp
#    |  |--__init__.py
#    |  |--models.py
#    |  |--views.py
#    |  |--templates
#    |     |--authapp
#    |        |--base.html
#    |        |--index.html
# Примечание: структуру файла config.yaml придумайте сами, его можно создать в любом текстовом редакторе «руками»
# (не программно); предусмотреть возможные исключительные ситуации, библиотеки использовать нельзя.
import os
my_list = []
with open('config.yaml', 'r', encoding='utf-8') as f:
    while True:
        line = f.readline().strip()
        if line:
            my_list.append(line)
        else:
            break
try:
    os.mkdir(my_list[0])
    for element in my_list[1:]:
        if '(' not in element:
            list_direct_first_level = element.split('[')[1].split(']')[0].split(',')
            for direct_first_level in list_direct_first_level:
                os.makedirs(f'{my_list[0]}/{element.split(" [")[0]}/{direct_first_level}')
        elif '(' in element:
            list_direct_next_level = element.split('[')[1].split('{')[0].split(',')
            next_direct = element.split('{')[1].split('}')[0]
            list_direct_next2_level = element.split('(')[1].split(')')[0].split(',')
            for direct_next_level in list_direct_next_level:
                os.makedirs(f'{my_list[0]}/{element.split(" [")[0]}/{direct_next_level}')
            for direct_next2_level in list_direct_next2_level:
                os.makedirs(f'{my_list[0]}/{element.split(" [")[0]}/{list_direct_next_level[-1]}/{next_direct}/'
                            f'{direct_next2_level}')
except FileExistsError as e:
    print('Такие папки уже существуют')
