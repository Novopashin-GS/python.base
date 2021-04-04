# Склонение слова
# Реализовать склонение слова «процент» во фразе «N процентов». Вывести эту фразу на экран
# отдельной строкой для каждого из чисел в интервале от 1 до 100:
# 1 процент
# 2 процента
# 3 процента
# 4 процента
# 5 процентов
# 6 процентов
# ...
# 100 процентов
for number in range(1, 101):
    if number >= 10 and number <= 20:
        print(f'{number} процентов')
    else:
        remainder = number % 10
        if remainder == 1:
            print(f'{number} процент')
        elif remainder >=2 and remainder <=4:
            print(f'{number} процента')
        else:
            print(f'{number} процентов')