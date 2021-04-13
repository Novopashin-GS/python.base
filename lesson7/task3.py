# 3. Создать структуру файлов и папок, как написано в задании 2 (при помощи скрипта или «руками» в проводнике).
# Написать скрипт, который собирает все шаблоны в одну папку templates, например:
# |--my_project
#    ...
#   |--templates
#    |   |--mainapp
#    |   |  |--base.html
#    |   |  |--index.html
#    |   |--authapp
#    |      |--base.html
#    |      |--index.html
# Примечание: исходные файлы необходимо оставить; обратите внимание, что html-файлы расположены в родительских папках
# (они играют роль пространств имён); предусмотреть возможные исключительные ситуации; это реальная задача,
# которая решена, например, во фреймворке django.
import shutil
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
print(my_list)
try:
    shutil.move(f'{my_list[0]}/mainapp/templates', f'{my_list[0]}/')
    shutil.move(f'{my_list[0]}/authapp/templates/authapp', f'{my_list[0]}/templates')
    os.rmdir(f'{my_list[0]}/authapp/templates')
except shutil.Error as y:
    print('такие папки уже существуют')
