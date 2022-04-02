from criptos.models import CriptoValorModel, ErrorApi
from criptos.vista import CriptoValorVista
from criptos.config import API_KEY

class CriptoValorControlador:
    def __init__(self):
        self.vista = CriptoValorVista()
        self.model = CriptoValorModel(API_KEY)

    def executa(self):
        self.vista.demana()
        self.model.origen = self.vista.origen
        self.model.desti = self.vista.desti
        try:
            self.model.obtenir_taxa()
            self.vista.ensenya(self.model.taxa)
        except ErrorApi as e:
            self.vista.error(e.args[0])


    
    