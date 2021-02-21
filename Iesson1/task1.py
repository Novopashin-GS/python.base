user_time = int(input('Ввеdите размер интервала (в секунdах)'))
second_in_minute = 60
second_in_hour = 3600
second_in_day = 86400
if user_time < 60:
    print(f'{user_time} cекунd')
elif user_time >= second_in_minute and user_time <second_in_hour:
    minute = user_time // second_in_minute
    second = user_time % second_in_minute
    print(f'{minute} мин {second} сек')
elif user_time >= second_in_hour and user_time < second_in_day:
    hour = user_time // second_in_hour
    minute = user_time % second_in_hour // second_in_minute
    second = user_time % second_in_hour % second_in_minute
    print(f'{hour} час {minute} мин {second} сек')
elif user_time >= second_in_day:
    day = user_time // second_in_day
    hour = user_time % second_in_day // second_in_hour
    minute = user_time % second_in_day % second_in_hour // second_in_minute
    second = user_time % second_in_day % second_in_hour % second_in_minute
    print(f' {day} dень {hour} час {minute} мин {second} сек')
else:
    print('Вы ввели некорректное время')
