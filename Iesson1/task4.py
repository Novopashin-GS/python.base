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
for namber in range(1,101):
    if namber >= 10 and namber <= 20:
        print(f'{namber} процентов')
    else:
        remainder = namber % 10
        if remainder == 1:
            print(f'{namber} процент')
        elif remainder >=2 and remainder <=4:
            print(f'{namber} процента')
        else:
            print(f'{namber} процентов')