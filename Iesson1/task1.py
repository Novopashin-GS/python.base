# Спросить у пользователя размер интервала (в секундах). Вывести на экран строку в зависимости от размера интервала:
# 1) до минуты: <s> сек;
# 2) до часа: <m> мин <s> сек;
# 3) до суток: <h> час <m> мин <s> сек;
# 4) сутки или больше: <d> дн <h> час <m> мин <s> сек
user_time = int(input('Ввеdите размер интервала (в секунdах)'))
second_in_minute = 60
second_in_hour = 3600
second_in_day = 86400
minute = user_time // 60
hour = minute // 60
day = hour // 24
second = user_time % 60
minute %= 60
hour %= 24
if user_time < second_in_minute:
    print(f'{user_time} cекунd')
elif user_time <second_in_hour:
    print(f'{minute} мин {second} сек')
elif user_time < second_in_day:
    second = user_time % second_in_hour % second_in_minute
    print(f'{hour} час {minute} мин {second} сек')
elif user_time >= second_in_day:
    print(f' {day} dень {hour} час {minute} мин {second} сек')
else:
    print('Вы ввели некорректное время')
