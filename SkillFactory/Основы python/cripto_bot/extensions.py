import json
import requests
from config import currency


class ConvertionException(Exception):
    pass

class Exchange:
    @staticmethod
    def get_price(quote, base, amount):
        if quote == base:
            raise ConvertionException(f'Перевод одинаковых валют не возможен')

        try:
            quote_ticker = currency[quote]
        except KeyError:
            raise ConvertionException(f'Такой валюты нет >>> {quote}')

        try:
            base_ticker = currency[base]
        except KeyError:
            raise ConvertionException(f'Такой валюты нет >>> {base}')

        try:
            if int(amount) > 0:
                amount = int(amount)
            else:
                raise ConvertionException(f'Введено отрицательное количество >>> {amount}')
        except ValueError:
            raise ConvertionException(f'Некорректно введено количество >>> {amount}')

        response = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={quote_ticker}&tsyms={base_ticker}')
        total_base = json.loads(response.content)[currency[base]]
        return float(total_base * amount)
