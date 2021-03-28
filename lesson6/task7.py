# 7. * (вместо 6) Добавить возможность редактирования данных при помощи отдельного скрипта:
# передаём ему номер записи и новое значение. При этом файл не должен читаться целиком — обязательное требование.
# Предусмотреть ситуацию, когда пользователь вводит номер записи, которой не существует.

import sys
start = (int(sys.argv[1])-1)
end = 0
with open('bakery.txt', 'r+', encoding='utf8') as f:
    for line in f:
        end += 1
with open('bakery.txt', 'r+', encoding='utf8') as f:
    if 10 * start < end * 10:
        f.seek(10*start)
        print(f'{sys.argv[2]:8}', file=f)
    else:
        print('Такой строки нет')
