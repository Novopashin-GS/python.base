# Задание 2
# Дан список:
# ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
# Необходимо его обработать — обособить каждое целое число (вещественные не трогаем) кавычками (добавить кавычку до и кавычку после элемента списка, являющегося числом) и дополнить нулём до двух целочисленных разрядов:
# ['в', '"', '05', '"', 'часов', '"', '17', '"', 'минут', 'температура', 'воздуха', 'была', '"', '+05', '"', 'градусов']
# Сформировать из обработанного списка строку:
# в "05" часов "17" минут температура воздуха была "+05" градусов
# Подумать, какое условие записать, чтобы выявить числа среди элементов списка? Как модифицировать это условие для чисел со знаком?
# Примечание: если обособление чисел кавычками не будет получаться - можете вернуться к его реализации позже. Главное: дополнить числа до двух разрядов нулём!




element = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
count = 0
variants = 0
number_plus_or_minus = 0
def add (element):
    element.insert(count + 1, "'")
    element.insert(count, "'")
while count < len(element):
    if element[count].find("+") != -1:
        number_plus_or_minus = count
        element[count] = element[count][1:]
        variants = 1
    elif element[count].find("-") != -1:
        number_plus_or_minus = count
        element[count] = element[count][1:]
        variants = 2
    if element[count].isdigit() == True:
        if len(element[count]) < 2:
            element[count] = '0' + element[count]
        if variants == 1:
            element[count] = '+' + element[count]
            add(element)
            variants = 0
        elif variants == 2:
            element[count] = '-' + element[count]
            add(element)
            variants = 0
        else:
            add(element)
        count += 1
    count += 1
print(element)
print(" ".join(element))
