# 2. * (вместо задачи 1) Доработать предыдущую функцию num_translate_adv(): реализовать корректную работу с числительными, начинающимися с заглавной буквы. Например:
# >>> >>> num_translate_adv("One")
# "Один"
# >>> num_translate_adv("two")
# "два"

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
    new_word = word.lower()
    if new_word[1:] == word[1:] and new_word[0].upper() == word[0]:
        return words[new_word][0].upper() + words[new_word][1:]
    elif new_word in words and new_word[0].upper() != word[0]:
        return words[new_word]
    else:
        return words.get(new_word)




word = input('Введите число от 0 dо 10 на английском языке: ')
print(num_translate(word))
