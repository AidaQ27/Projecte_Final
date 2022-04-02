import requests
from balance import URL_TASA_ESPECIFICA
from criptos.errors import ErrorApi, CONNECT_ERROR

class CriptoValorModel:
    def __init__(self, apikey ,origen = '', desti = ''):
        self.apikey = apikey
        self.origen = origen
        self.desti = desti

        self.taxa = 0.0

    
    def obtenir_taxa(self):
        try:
            resposta = requests.get(URL_TASA_ESPECIFICA.format(self.origen, self.desti, self.apikey))

        except:
            raise ErrorApi(CONNECT_ERROR)

        if resposta.status_code != 200:
            raise ErrorApi(resposta.status_code, resposta.json()['error'])

        self.taxa = round(resposta.json()['rate'], 2)