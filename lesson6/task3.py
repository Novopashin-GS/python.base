# 3. Есть два файла: в одном хранятся ФИО пользователей сайта, а в другом — данные об их хобби.
# Известно, что при хранении данных используется принцип: одна строка — один пользователь, разделитель между значениями
# — запятая. Написать код, загружающий данные из обоих файлов и формирующий из них словарь: ключи — ФИО, значения —
# данные о хобби. Сохранить словарь в файл. Проверить сохранённые данные. Если в файле, хранящем данные о хобби,
# меньше записей, чем в файле с ФИО, задаём в словаре значение None. Если наоборот — выходим из скрипта с кодом «1».
# При решении задачи считать, что объём данных в файлах во много раз меньше объема ОЗУ.
# Фрагмент файла с данными о пользователях (users.csv):
# Иванов,Иван,Иванович
# Петров,Петр,Петрович
# Фрагмент файла с данными о хобби (hobby.csv):
# скалолазание,охота
# горные лыжи


count_line_name = 0
count_line_hobby = 0
users = {}
with open("users.csv", 'r', encoding='utf8') as f:
    with open("hobby.csv", 'r', encoding='utf8') as f1:
        for line_name in f:
            count_line_name += 1
        for line_hobby in f1:
            count_line_hobby += 1
with open("users.csv", 'r', encoding='utf8') as f:
    with open("hobby.csv", 'r', encoding='utf8') as f1:
        if count_line_hobby == count_line_name:
            for line_name in f:
                line_name = line_name.strip().replace(',', ' ')
                line_hobby = f1.readline().strip()
                users[line_name] = line_hobby
        elif count_line_hobby > count_line_name:
            exit(1)
        else:
            for line_name in f:
                line_name = line_name.strip().replace(',', ' ')
                line_hobby = f1.readline().strip()
                if line_hobby:
                    users[line_name] = line_hobby
                else:
                    users[line_name] = None
print(users)
