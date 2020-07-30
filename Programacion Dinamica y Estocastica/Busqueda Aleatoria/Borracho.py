#Camino del borracho
import random



class Borracho:

    def __init__(self, nombre):
        self.nombre = nombre


class BorrachoTradicional(Borracho):

    def __init__(self, nombre):
        super().__init__(nombre)

    #Retorna tupla
    def camina(self):
        return random.choice([(0, 1), (0, -1), (1, 0), (-1, 0)])
