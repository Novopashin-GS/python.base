# Задание 2. Курс Валюты
# Написать функцию get_currency_rate(), принимающую в качестве аргумента код валюты
# (например, USD, EUR, GBP, ...) в виде строки и возвращающую курс этой валюты по отношению к рублю.
# Код валюты может быть в произвольном регистре.
# Функция должна возвращать результат числового типа, например float.
# Если в качестве аргумента передали код валюты, которого нет в ответе, вернуть None.
# Используйте библиотеку requests, чтобы забрать актуальные данные из ЦБ РФ по адресу
# http://www.cbr.ru/scripts/XML_daily.asp.
#
# Выведите на экран курсы для доллара и евро, используя написанную функцию.
#
# Рекомендация: выполнить предварительно запрос к этой странице в обычном браузере,
# посмотреть содержимое ответа.

import requests


def get_currency_rate(valute):
    site = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
    text = site.content.decode('windows-1251')
    str_valute = text.split('</Valute><Valute')
    valute_code = '<CharCode>' + valute.upper() + '</CharCode>'
    for need_str in str_valute:
        if valute_code in need_str:
            break
    else:
        return print('None')

    one_part_text, second_part_text = need_str.split('<Value>')
    one_part_valute, second_part_valute = second_part_text.split('</Value>')
    print(float(one_part_valute.replace(',', '.')))


get_currency_rate('GBP')
