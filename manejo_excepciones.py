"""
Son muy comunes en la programación. no tienen nada de excepcional.
Las excepciones de Python normalmente se relacionan con errores de semántica.
Se puede crear excepciones propias.
Cuando una excepcion no se maneja (unhandled exception), el programa termnia en error.

Las excepciones se manejan con los keywords:
    try
    except
    finally

Se peuden utilizar también para ramificar programas.
No deben manejarse de manera silenciosa (po ejemplo, con print statements).
Para aventar tu propia excepcion utiliza el keyword raise.

"""

def divide_elementos_de_lista(lista, divisor):
    try:
        return [i / divisor for i in lista]
    except ZeroDivisionError as e: #Se agrega un excepcion de la division entre cero, por tanto si el divisor es 0 entregará la lista original
        print(e) #Entrega el tipo de error
        return lista

lista = list(range(10))
divisor = 0


print(divide_elementos_de_lista(lista, divisor))