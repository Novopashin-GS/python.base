# Задание 5
# Создать вручную список, содержащий цены на товары (10–20 товаров), например:
# [57.8, 46.51, 97, ...]
# Вывести на экран эти цены через запятую в одну строку, цена должна отображаться в виде <r> руб <kk> коп.
# Например:
# 57 руб 08 коп, 46 руб 51 коп, 97 руб 00 коп, ...
# Подумать, как из цены получить рубли и копейки, как добавить нули, если, например, получилось 7 копеек или 0 копеек (должно быть 07 коп или 00 коп).
# Вывести цены, отсортированные по возрастанию, новый список не создавать (доказать, что объект списка после сортировки остался тот же).
# Создать новый список, содержащий те же цены, но отсортированные по убыванию.
# Вывести цены пяти самых дорогих товаров. Сможете ли вывести цены этих товаров по возрастанию, написав минимум кода?


random_number = [57.8, 46.51, 97, 13.1, 22.15, 65.99, 72.62, 88.9, 43.57, 71.73, 82.13, 99.99, 5.56]
for i in range(0, len(random_number)):
    random_number[i] = str(float(random_number[i]))
    random_number[i] = random_number[i].split('.')
    if len(random_number[i][0]) < 2:
        random_number[i][0] = '0' + random_number[i][0]
    if len(random_number[i][1]) < 2:
        random_number[i][1] = '0' + random_number[i][1]
    random_number[i][0] = random_number[i][0] + "руб"
    random_number[i][1] = random_number[i][1] + "коп"
    random_number[i] = " ".join(random_number[i])
print(", ".join(random_number))
print(id(random_number))
# Вывести цены, отсортированные по возрастанию, новый список не создавать (доказать, что объект списка после сортировки остался тот же).
print(random_number)
random_number.sort()
print(id(random_number))
# Создать новый список, содержащий те же цены, но отсортированные по убыванию.
print(random_number)
random_number_s = list(reversed(random_number))
print(random_number_s)
# Вывести цены пяти самых дорогих товаров. Сможете ли вывести цены этих товаров по возрастанию, написав минимум кода?
print(random_number_s[4::-1])




