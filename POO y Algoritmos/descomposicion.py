
class Automovil:

    def __init__(self, modelo, marca, color):
        self.modelo = modelo
        self.marca = marca
        self.color = color
        self._estado = 'en_reposo'
        self._motor = Motor(cilindros=4)
        self._asiento = Asiento(cantidad=5, material='sintetico')
        self._temperatura = Motor(cilindros=2)

    def acelerar(self, tipo='despacio'):
        if tipo == 'rapida':
            self._motor.inyecta_gasolina(10)
        else:
            self._motor.inyecta_gasolina(3)
        
        self._estado = 'en_movimiento'

    def frenado(self, tipo='moderado'):
        if tipo == 'brusco':
            self._temperatura = 7
            print(f'Frena mas despacio. La temperatura se elevó a {self._temperatura}')

class Motor:

    def __init__(self, cilindros, tipo='gasolina'):
        self.cilindros = cilindros
        self.tipo = tipo
        self._temperatura = 0

    def inyecta_gasolina(self, cantidad):
        pass

class Asiento:

    def __init__(self, cantidad, material):
        self.cantidad = cantidad
        self.material = material
        self._densidad = 'Normal'

if __name__ == '__main__':
    car = Automovil('Yaris', 'Toyota', 'Plateado')
    car._motor.tipo = 'Diesel'
    print(car._motor.tipo)
    car.acelerar('lenta')
    car.frenado('brusco')