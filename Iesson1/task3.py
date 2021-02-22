# Создать список, состоящий из кубов нечётных чисел от 0 до 1000 (куб X - третья степень числа X):
my_list = []
def remainder(my_list):
    total = 0
    count = 0
    for element in my_list:
        i = element
        while element != 0:
            count = count + element % 10
            element = element // 10
        if count % 7 == 0:
            total = total + i
        count = 0
    return total
for namber in range(1,1000,2):
    my_list.append(namber**3)
print(my_list)
# 1) Вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7.
# Например, число «19 ^ 3 = 6859» будем включать в сумму, так как 6 + 8 + 5 + 9 = 28 – делится нацело на 7.
# Внимание: использовать только арифметические операции!
print(remainder(my_list))
# 2) К каждому элементу списка добавить 17 и заново вычислить сумму тех чисел из нового списка,
# сумма цифр которых делится нацело на 7.
my_list2 = my_list[:]
for index in range(len(my_list)):
    my_list2[index] = my_list[index]+17
print(my_list2)
print(remainder(my_list2))
# 3) Написать алгоритм вычисляющий то же значение суммы, что и в пункте 2), но не создавая списков
count = 0
total = 0
for element in my_list:
    element += 17
    i = element
    while element != 0:
        count = count + element % 10
        element = element // 10
    if count % 7 == 0:
        total = total + i
    count = 0
print(total)





