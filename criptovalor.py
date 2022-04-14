import requests

endpoint= ("https://rest.coinapi.io/v1/exchangerate/{}/{}?apikey={}")

moneda_from = input('Moneda de origen: ')
moneda_to = input('Moneda a conseguir: ')
api_key = '05BF565B-CA92-421A-AF57-699C95894ACE'

resposta = requests.get(endpoint.format(moneda_from, moneda_to, api_key))

print((resposta.json()['rate']))

