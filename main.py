import requests

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
parameters = {
    'start': '1',
    'limit': '5000',
    'convert': 'USD'
}
headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': 'd3bd9692-75a3-4c6e-87d3-6a70266055c3',
}

response = requests.get(url, headers=headers).json()
data = response
print(data)
