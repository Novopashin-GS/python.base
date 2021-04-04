# Задание 1. Функция-генератор rand_nums
# Написать функцию-генератор rand_nums, генерирующую N случайных целых чисел в диапазоне 1 до 100 (включительно).
# Количество чисел N, которое выдаст генератор передается в функцию через параметр:
#
# >>> rand15 = rand_nums(15)
# >>> next(rand15) # 1-й вызов
# 11
# >>> next(rand15) # 2-й вызов
# 38
# ...
# >>> next(rand15) # 15-й вызов
# 7
# >>> next(rand15) # 16-й вызов
# ...StopIteration...

import random


def rand_nums(n):
    count = 1
    while count <= n:
        yield random.randint(1, 100)
        count += 1


if __name__ == "__main__":
    rand10 = rand_nums(10)
    for i in range(11):
        print(i+1, next(rand10))
