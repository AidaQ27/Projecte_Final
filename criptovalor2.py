from criptos.models import CriptoValorModel
from criptos.vista import CriptoValorVista
from criptos.errors import ErrorApi

vista = CriptoValorVista()
vista.demana()

cvm = CriptoValorModel(vista.origen, vista.desti)
try:
    cvm.obtenir_taxa()
    print(cvm.taxa)
except ErrorApi:
    print('No es pot calcular la taxa')