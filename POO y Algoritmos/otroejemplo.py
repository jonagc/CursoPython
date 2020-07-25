class Coche:

    def __init__(self):
        self.largoChasis = 250
        self.anchoChasis = 120
        self.ruedas = 4
        self.enmarcha = False

    def arrancar(self, arrancamos):
        self.enmarcha = arrancamos

        if(self.enmarcha):
            return 'EL coche está en marcha'
        else:
            return 'El coche está parado'

    
    def estado(self):
        print(f'El coche tiene {self.ruedas} ruedas. Un ancho de {self.anchoChasis} y un largo de {self.largoChasis}')


miCoche = Coche()

print(miCoche.arrancar(True))
miCoche.estado()

print('------------------------A continuación creamos el segundo objeto-----------------------------------')

miChoche2 = Coche()

print(miChoche2.arrancar(False))

miChoche2.ruedas = 2

miChoche2.estado()



