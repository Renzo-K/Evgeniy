# Дан список, необходимо его обработать — обособить каждое число кавычками и дополнить нулём до двух целочисл. разрядов

weather_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
# флаг
num = 0
# Перебираем список по индексам
for i in range(len(weather_list)):
    i += num
    # Ищем числа
    if weather_list[i][-1].isdigit():
        # Дополняем найденное число нулём
        if weather_list[i][0] in '+':
            weather_list[i] = f'{weather_list[i][0]}{int(weather_list[i]):02}'
        else:
            weather_list[i] = f'{int(weather_list[i]):02}'
        # Дополняем число кавычками
        weather_list.insert(i, '"')
        weather_list.insert(i + 2, '"')
        # Корректируем индекс
        num += 2

# Формируем из обработанного списка строку
for i in weather_list:
    i.split(',')
    print(i, end=' ')
