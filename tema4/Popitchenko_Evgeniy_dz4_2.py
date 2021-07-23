from requests import get, utils
from datetime import date, datetime


def currency_rates(code):

    response = get('http://www.cbr.ru/scripts/XML_daily.asp')
    encodings = utils.get_encoding_from_headers(response.headers)
    content = response.content.decode(encoding=encodings)

    result = content.split('<Valute')
    d, m, y = result[0].split('"')[-4].split('.')

    for i in result:
        if code.upper() in i:
            print(date(day=int(d), month=int(m), year=int(y)))
            return float(i.replace('/', '').split('<Value>')[1].replace(',', '.'))

print(currency_rates('USD'))
