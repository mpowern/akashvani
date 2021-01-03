import json


import requests

TICKER_API_URL = 'https://api.coinmarketcap.com/v1/ticker/'
crypto = 'bitcoin'


def get_latest_crypto_price(coin):
    response = requests.get(TICKER_API_URL + coin)
    response_json = response.json()

    return float(response_json[0]['price_usd'])


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    last_price = -1

    while True:

        price = get_latest_crypto_price(crypto)

        if price != last_price:
            print('Bitcoin price: ', price)
            last_price = price
