
import requests
import sqlite3
from criptos.errors import ErrorApi, CONNECT_ERROR
from datetime import datetime

now = datetime.now()

class CriptoValorModel:
    def __init__(self, apikey ,origen = '', desti = ''):
        self.apikey = apikey
        self.origen = origen
        self.desti = desti
        self.temps = now.time()
        

        self.taxa = 0.0

    
    def obtenir_taxa(self):
        try:
            resposta = requests.get("https://rest.coinapi.io/v1/exchangerate/{}/{}?time={}apikey={}".format(self.origen, self.desti, self.temps, self.apikey))
            # https://rest.coinapi.io/v1/exchangerate/EUR/BTC?time={}apikey=05BF565B-CA92-421A-AF57-699C95894ACE
        except:
            raise ErrorApi(CONNECT_ERROR)

        if resposta.status_code != 200:
            raise ErrorApi(resposta.status_code, resposta.json()['error'])

        self.taxa = round(resposta.json()['rate'], 2)

        return self.taxa

    def obtenir_quantitat(self, quantitat_from):

        return self.obtenir_taxa() * quantitat_from
        

class ProcesaDades:

    def recupera_dades_moviments(self):
            con = sqlite3.connect('data/movimientos.db')
            cur = con.cursor()

            cur.execute("""
                            SELECT fecha,hora,moneda_from,cantidad_from,moneda_to,cantidad_to,precio
                            FROM moviments
                            ORDER BY fecha;
                        """
            )
            

            return cur.fetchall()
       

        