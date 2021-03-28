# 4. * (вместо 3) Решить задачу 3 для ситуации, когда объём данных в файлах превышает объём ОЗУ
# (разумеется, не нужно реально создавать такие большие файлы, это просто задел на будущее проекта).
# Также реализовать парсинг данных из файлов - получить отдельно фамилию, имя и отчество для пользователей и название
# каждого хобби: преобразовать в какой-нибудь контейнерный тип (список, кортеж, множество, словарь). Обосновать выбор
# типа. Подумать, какие могут возникнуть проблемы при парсинге. В словаре должны храниться данные, полученные в
# результате парсинга.


count_line_name = 0
count_line_hobby = 0
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
                line_hobby = list(f1.readline().strip().split(','))
                print(line_name, line_hobby)
        elif count_line_hobby > count_line_name:
            exit(1)
        else:
            for line_name in f:
                line_name = line_name.strip().replace(',', ' ')
                line_hobby = f1.readline().strip()
                if line_hobby:
                    print(line_name, list(line_hobby.split(',')))
                else:
                    print(line_name, None)
