
class Campo:
#Donde se mueve el borracho

    def __init__(self):
        self.coordenadas_de_borrachos = {}
    #Agrega borracho al diccionario
    def anadir_borracho(self, borracho, coordenada):
        self.coordenadas_de_borrachos[borracho] = coordenada

    #Mueve el borracho de coordenadas
    def mover_borracho(self, borracho):
        delta_x, delta_y = borracho.camina()
        coordenada_actual = self.coordenadas_de_borrachos[borracho]
        nueva_coordenada = coordenada_actual.mover(delta_x, delta_y)

        self.coordenadas_de_borrachos[borracho] = nueva_coordenada

    #Retorna la coordenada del borracho
    def obtener_coordenada(self, borracho):
        return self.coordenadas_de_borrachos[borracho]