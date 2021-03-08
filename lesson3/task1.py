# 1. Написать функцию num_translate(), переводящую числительные от 0 до 10 c английского на русский язык. Например:
#  num_translate("one")
# "один"
# num_translate("eight")
# "восемь"
# Если перевод сделать невозможно, вернуть None. Подумайте, как и где лучше хранить информацию, необходимую для перевода: какой тип данных выбрать, в теле функции или снаружи.

#В dанной заdаче лучше хранить информацию в виdе списка, а созdать его лучше снаружи функции, чтобы не созdавать кажdый раз
words = {
    'zero': "ноль",
    'one': "один",
    'two': "два",
    'three': "три",
    'four': "четыре",
    'five': "пять",
    'six': "шесть",
    'seven': "семь",
    'eight': "восемь",
    'nine': "девять",
    'ten': "десять"
}


def num_translate(word):
    return words.get(word)


word = input('Введите число от 0 dо 10 на английском языке: ')
print(num_translate(word))