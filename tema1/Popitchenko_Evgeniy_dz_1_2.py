# создание списка кубов нечётных чисел от 1 до 1000

numbers = []
coub_sum = 0
for number in range(1, 1000, 2):
    numbers.append(number ** 3)
for coub in numbers:
    singl = 0
    i = coub

# разбираем число по цифрам

    while coub != 0:
        singl += coub % 10
        coub //= 10

# складываем числа кратные 7

    if singl % 7 == 0:
        coub_sum += i

print(coub_sum)

# добавляем 17 к каждому элементу списка
coub17 = []
coub_sum = 0
for coub in numbers:
    coub17.append(coub + 17)

# перебираем новый список

for coub in coub17:
    i = coub
    singl = 0

# разбираем число по цифрам

    while coub != 0:
        singl += coub % 10
        coub //= 10
    if singl % 7 == 0:
        coub_sum += i

print(coub_sum)

# задача под пунктом b, не создавая нвоый список (загуглил как это сделать))

for key, number in enumerate(numbers):
    numbers[key] = number + 17

    while coub != 0:
        singl += coub % 10
        coub //= 10
    if singl % 7 == 0:
        coub_sum += i

print(coub_sum)