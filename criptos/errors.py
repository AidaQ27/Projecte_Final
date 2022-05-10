CONNECT_ERROR = 699

class ErrorApi(Exception):
    def error(self, codigo):
        if codigo == 400:
            print('Hay algo erróneo en tu petición')
        elif codigo == 401:
            print('No autorizado - Tu APIKEY es erronea')
        elif codigo == 403:
            print('Prohibido - Tu API no tiene acceso a esta funcionalidad')
        elif codigo == 429:
            print('Has excedido el límite de peticiones')
        elif codigo == 550:
            print('Sin datos - la moneda introducida no existe')
        elif codigo == 699:
            print(' hay problemas para comunicarse en la BBDD. INTENTALO DE NUEVO MÁS TARDE')
        else: 
            print('{}, no sabemos que es este codigo'. format(codigo))