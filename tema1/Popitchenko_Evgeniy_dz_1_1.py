# преобразования секунд в дни/часы/минуты

duration = int(input('Введите кол-во секунд: '))

if duration < 60:
    print(f'{duration} сек')
elif 3600 > duration >= 60:
    print(f'{duration // 60} мин {duration % 60} сек')
elif 86400 > duration >= 3600:
    print(f'{duration // 3600} час {duration % 3600 // 60} мин {duration % 60} сек')
elif duration >= 86400:
    print(f'{duration // 86400} дн {duration % 86400 // 3600} час {duration % 3600 // 60} мин {duration % 60} сек')
