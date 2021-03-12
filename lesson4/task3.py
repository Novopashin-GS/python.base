# Задание 3. * Курс Валюты (расширенный)
# Доработать функцию get_currency_rate(): теперь она должна возвращать курс и дату,
# на которую этот курс действует (взять из того же файла ЦБ РФ).
# Для значения курса используйте тип Decimal (https://docs.python.org/3.8/library/decimal.html) вместо float.
# Дата должна быть типа datetime.date.

import datetime
import requests
import decimal

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
    print(decimal.Decimal(one_part_valute.replace(',', '.')))
    one_part_text_day, second_part_text_day = text.split('Date="')
    one_part_text_need_day, second_part_text_need_day = second_part_text_day.split('" name')
    day, month, year = list(map(int, one_part_text_need_day.split('.')))
    date = datetime.date(year, month, day)
    print(date)


get_currency_rate('GBP')
