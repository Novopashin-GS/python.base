# 5. ** (вместо 4) Решить задачу 4 и реализовать интерфейс командной строки, чтобы можно было задать путь
# к обоим исходным файлам и путь к выходному файлу со словарём. Проверить работу скрипта для случая, когда все файлы
# находятся в разных папках.


import sys
count_line_name = 0
count_line_hobby = 0
with open(sys.argv[1], 'r', encoding='utf8') as f:
    with open(sys.argv[2], 'r', encoding='utf8') as f1:
        for line_name in f:
            count_line_name += 1
        for line_hobby in f1:
            count_line_hobby += 1
with open(sys.argv[1], 'r', encoding='utf8') as f:
    with open(sys.argv[2], 'r', encoding='utf8') as f1:
        with open(sys.argv[3], 'w', encoding='utf8') as f2:
            if count_line_hobby == count_line_name:
                for line_name in f:
                    line_name = line_name.strip().replace(',', ' ')
                    line_hobby = list(f1.readline().strip().split(','))
                    print(line_name, line_hobby, file=f2)
            elif count_line_hobby > count_line_name:
                exit(1)
            else:
                for line_name in f:
                    line_name = line_name.strip().replace(',', ' ')
                    line_hobby = f1.readline().strip()
                    if line_hobby:
                        print(line_name, list(line_hobby.split(',')), file=f2)
                    else:
                        print(line_name, None, file=f2)
