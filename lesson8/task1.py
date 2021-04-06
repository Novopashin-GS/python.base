# 1. Написать функцию email_parse(<email_address>), которая при помощи регулярного выражения извлекает имя пользователя
# и почтовый домен из email адреса и возвращает их в виде словаря. Если адрес не валиден, выбросить исключение
# ValueError. Пример:
# >>> email_parse('someone@geekbrains.ru')
# {'username': 'someone', 'domain': 'geekbrains.ru'}
# >>> email_parse('someone@geekbrainsru')
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#   ...
#     raise ValueError(msg)
# ValueError: wrong email: someone@geekbrainsru
# Примечание: подумайте о возможных ошибках в адресе и постарайтесь учесть их в регулярном выражении;
# имеет ли смысл в данном случае использовать функцию re.compile()?


import re
my_dict = {}


def email_parse(email_address):
    name = re.search(r"^([\w+-]+)@(\w+\.\w+)$", email_address)
    if name:
        my_dict.setdefault('username', name.groups()[0])
        my_dict.setdefault('domain', name.groups()[1])
        print(my_dict)
    else:
        raise ValueError


email_parse('some_1-one@geekbrains.ru')
