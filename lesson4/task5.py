# Задание 5. * Вызов с командной строки
# Доработать скрипт из предыдущего задания: теперь он должен работать и из консоли,
# а коды валют ему дожны передавать через аргументы командной строки (там может быть один или несколько кодов).
# Вывод курсов сделать в том же порядке, что присланные аргументы
# Например:
#
# python task5.py USD EUR
# USD 75.18, 2020-09-05
# EUR 80.35, 2020-09-05

import datetime
import requests
import decimal
import sys


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
    one_part_text_day, second_part_text_day = text.split('Date="')
    one_part_text_need_day, second_part_text_need_day = second_part_text_day.split('" name')
    day, month, year = list(map(int, one_part_text_need_day.split('.')))
    date = datetime.date(year, month, day)
    print(f"{decimal.Decimal(one_part_valute.replace(',', '.'))}, {date}")


get_currency_rate(sys.argv[1])
