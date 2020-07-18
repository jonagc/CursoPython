#Definición

class Persona:

    def __init__(self, nombre, edad):
        self.nombre = nombre #Inicializar variables de instancia. Se ocupa self para hacer referencia a la misma clase
        self.edad = edad
        
    def saluda(self, otra_persona):
        return f'Hola {otra_persona.nombre}, me llamo {self.nombre}.'


#Uso

>>> david = Persona('David', 35)
>>> erika = Persona('Erika', 32)

>>> david.saluda(erika)
#Hola Erika, me llamo David

class Coordenadas:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distancia(self, otra_coordenada):
        x_diff = (self.x - otra_coordenada.x)**2
        y_diff = (self.y - otra_coordenada.y)**2

        return (x_diff + y_diff)**0.5

if __name__ == '__main__':
    coord_1 = Coordenadas(3, 20)
    coord_2 = Coordenadas(4, 10)

    print(coord_1.distancia(coord_2))
    print(isinstance(coord_2, Coordenadas))