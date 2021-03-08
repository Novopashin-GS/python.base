# 5. Реализовать функцию get_jokes(), возвращающую n шуток, сформированных из трех слов, взятых из трёх списков (по одному слову из каждого списка):
# nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
# adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
# adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
#         Например:
# >>> get_jokes(2)
# ["лес завтра зеленый", "город вчера веселый"]
# Документировать код функции.
# Сможете ли вы добавить еще один аргумент — флаг, разрешающий или запрещающий повторы слов в шутках (когда каждое слово можно использовать только в одной шутке)? Сможете ли вы сделать аргументы именованн5. Реализовать функцию get_jokes(), возвращающую n шуток, сформированных из трех слов, взятых из трёх списков (по одному слову из каждого списка):
# nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
# adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
# adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
#         Например:
# >>> get_jokes(2)
# ["лес завтра зеленый", "город вчера веселый"]
# Документировать код функции.
# Сможете ли вы добавить еще один аргумент — флаг, разрешающий или запрещающий повторы слов в шутках (когда каждое слово можно использовать только в одной шутке)? Сможете ли вы сделать аргументы именованными?


nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
import random


def get_jokes(quantity, key=False):
    '''
    Функция генериует шутки из заdанных списков

    :param quantity: количество шуток
    :param key: флаг, разрешающий или запрещающий повторы слов в шутках
    :return: возвращает список с шутками
    '''
    jokes = []
    i = 0
    while i < quantity:
        noun = nouns[random.randrange(len(nouns))]
        adverb = adverbs[random.randrange(len(adverbs))]
        adjective = adjectives[random.randrange(len(adjectives))]
        jokes.append(f'{noun} {adverb} {adjective}')
        if key:
            nouns.remove(noun)
            adverbs.remove(adverb)
            adjectives.remove(adjective)
        i += 1
    return jokes


print(get_jokes(quantity=3, key=True))
print(get_jokes(quantity=4))

