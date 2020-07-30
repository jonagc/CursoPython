"""
Programacion orientada a objetos.
Permite definir tipos propios.
Permite maneja datiso y logica en un solo contenedor.
Las clases don como fabricas (moldes) para crear otro objetos.

Los objetos tienei atributos que se pueden definir al momento de INICIALIZAR un nuevo objeto o directamenteo en la INSTANCIA.
Las clases pueden tener varias varibles de clase, variables de instancia y variables locales.
Aunque Python no tiene el concepto de variables privadas integrado al lenguaje, es practica comun definirlas con un guion bajo.

isinstance y hasttr.


Los metodos son como funciones que tienen sentido unicamente ewn el contexto de una clase.
Al igual que las variables, los metodos privados se definen con un guion bajo.
La ENCAPSULACIÓN es un concepto clave de la programacion orientada a objetos:
    La forma practica de aplica este principio es declara todas la variables y metodos como privados, a menos que sea necesario exponerlos a otros programadores.
Un metodo clave que casi todas las clases deben tener es __init__
Otro es __str__
Existen varios tipos de metodos, estaticos, de clase, de instancia, getters y setters.


"""
class Lamp:
    _LAMPS = ['''
            .
         .    |    ,
          \   '   /
           ` ,-. '
        --- (   ) ---
             \ /
            _|=|_
           |_____|
        ''',
              '''
             ,-.
            (   )
             \ /
            _|=|_
           |_____|

    ''']
    def __init__(self, _is_turned_on): #metodo de construccion con self llamando a su propia instancia
        self._is_turned_on = _is_turned_on

    def turn_on(self):
        self._is_turned_on = True
        self._display_imagen()

    def turn_off(self):
        self._is_turned_on = False
        self._display_imagen()

    def _display_imagen(self):
        if self._is_turned_on:
            print(self._LAMPS[0])
        else:
            print(self._LAMPS[1])

def run():
    lamp = Lamp(_is_turned_on = True)

    while True:
        command = str(input('''
        ¿Qué desea hacer?

        [p]render
        [a]pagar
        [s]alir

              
        '''))

        if command == 'p':
            lamp.turn_on()
        elif command == 'a':
            lamp.turn_off()
        else:
            break


if __name__ == '__main__':
    run()


