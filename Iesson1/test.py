element = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
count = 0
variants = None
while count < len(element):
    if element[count].find("+") != -1:
        number_plus_or_minus = count
        element[count] = element[count][element[count].find("+") + 1:]
        variants = 1
    elif element[count].find("-") != -1:
        number_plus_or_minus = count
        element[count] = element[count][element[count].find("-") + 1:]
        variants = 2
    if element[count].isdigit() == True:
        if len(element[count]) < 2:
            element[count] = '0' + element[count]
        element.insert(count + 1, "'")
        element.insert(count, "'")
        count += 1
    count += 1
if variants == 1:
    element[number_plus_or_minus + 1] = "+" + element[number_plus_or_minus + 1]
    print(" ".join(element))
elif variants == 2:
    element[number_plus_or_minus + 1] = "-" + element[number_plus_or_minus + 1]
    print(" ".join(element))
else:
    print(" ".join(element))




