# 3. Написать декоратор для логирования типов позиционных аргументов функции, например:
# def type_logger...
#     ...
#
#
# @type_logger
# def calc_cube(x):
#    return x ** 3
#
# >>> a = calc_cube(5)
# 5: <class 'int'>
# Примечание: если аргументов несколько - выводить данные о каждом через запятую; можете ли вы вывести тип значения
# функции? Сможете ли решить задачу для именованных аргументов? Сможете ли вы замаскировать работу декоратора?
# Сможете ли вывести имя функции, например, в виде:
# >>> a = calc_cube(5)
# calc_cube(5: <class 'int'>)

from functools import wraps


def type_logger(func):

    @wraps(func)
    def logger(*args, **kwargs):
        if args and kwargs:
            need_list = []
            for element in args:
                res = func(element)
                need_list.append(f'{element}:{type(element)} ----> {res}:{type(res)}')
            for element in kwargs.values():
                res = func(element)
                need_list.append(f'{element}:{type(element)} ----> {res}:{type(res)}')
            print(f"{func.__name__}({', '.join(need_list)})")
        elif kwargs:
            need_list = []
            for element in kwargs.values():
                res = func(element)
                need_list.append(f'{element}:{type(element)} ----> {res}:{type(res)}')
            print(f"{func.__name__}({', '.join(need_list)})")
        elif args:
            need_list = []
            for element in args:
                res = func(element)
                need_list.append(f'{element}:{type(element)} ----> {res}:{type(res)}')
            print(f"{func.__name__}({', '.join(need_list)})")
    return logger


@type_logger
def calc_cube(x):
    return x ** 3


calc_cube(3)
print(calc_cube)
