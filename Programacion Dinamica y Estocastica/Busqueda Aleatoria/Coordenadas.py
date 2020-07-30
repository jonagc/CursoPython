class Coordenadas:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    #Retorna nueva coordenadas con la nueva posicion
    def mover(self, delta_x, delta_y):
        return Coordenadas(self.x + delta_x, self.y + delta_y)

    #Calcula la distancia entre ambas coordenadas (pitagoras)
    def distancia(self, otra_coordenada):
        delta_x = self.x - otra_coordenada.x
        delta_y = self.y - otra_coordenada.y

        return (delta_x**2 + delta_y**2)**0.5
