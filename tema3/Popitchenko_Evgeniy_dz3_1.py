numbers = {
    'one': 'один', 'two': 'два', 'three': 'три', 'four': 'четыре', 'five': 'пять', 'six': 'шесть', 'seven': 'семь',
    'eight': 'восемь', 'nine': 'девять', 'ten': 'десять'
}


def num_translate(number, dict):

    for k, v in dict.items():
        if k == number:
            print(v)
            break
    else:
        print('None')


num_translate(input('Enter number: ') ,numbers)