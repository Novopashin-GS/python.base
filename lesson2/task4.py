# Задание 4
# Дан список, содержащий искажённые данные с должностями и именами сотрудников:
# ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
# Известно, что имя сотрудника всегда в конце строки. Сформировать из этих имён и вывести на экран фразы вида: 'Привет, Игорь!
# Подумать, как получить имена сотрудников из элементов списка, как привести их к корректному виду. Можно ли при этом не создавать новый список?

names = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
size = len(names)
i = 0
while i < size:
    names[i] = names[i].split()
    end = len(names[i])-1
    names[i][end] = names[i][end].capitalize()
    print(f"Привет, {names[i][end]}")
    i += 1
