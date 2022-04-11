from flask import Flask

app = Flask(__name__)
app.secret_key = b'supersegura'

from balance.routes import *


URL_TASA_ESPECIFICA = "https://rest.coinapi.io/v1/exchangerate/{}/{}?apikey={}"

MONEDAS = ['EUR', 'ETH', 'BNB', 'LUNA', 'SOL', 'BTC', 'BCH', 'LINK', 'ATOM', 'USDT']

