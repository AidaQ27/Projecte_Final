from balance import MONEDAS

class CriptoValorVista:

    def __init__(self):
        self.origen = ''
        self.desti = ''
    
    def demana(self):
        origen = input('Moneda origen: ')
        while origen not in MONEDAS:
            print('La moneda debe ser una se las siguientes: ')
            print(' <-- '.join(MONEDAS))
            origen = input('Moneda origen: ')
        
        self.origen = origen

        desti = input('Moneda desti: ')
        while desti not in MONEDAS:
            print('La moneda debe ser una se las siguientes: ')
            print(' <-- '.join(MONEDAS))
            desti = input('Moneda desti: ')
        
        self.desti = desti

    
    def ensenya(self, taxa):
        print('1 {} son {:.2f} {}'.format(self.origen, taxa, self.desti))


            