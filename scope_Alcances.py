""" Scope o Alcance

Se refiere al alcance que tienen las variables en el código:

1.- alcance global: variables que se encuentra al principio de código, la cual se puede utilizar en cualquier función o apartado del código.
2.- alcance local: variable que es creada dentro de la función y que solo es reconocida dentro de esa función

"""

""" Especificaciones de código

Se le llama docstring o documentación y se estructura de la siguiente manera:
 1.- en la primera parte o línea va una descripción clara y concisa de la función y su funcionamiento
 2.- En medio se agrega la descripción de los diferentes parámetros, su tipo, su nombre y que es lo que se espera de esos parámetros
 3.- Por último se agrega lo que devuelve la función
"""

#Ejemplo de Especificación de código o docstring

def suma(a,b):
    """ Suma dos valores a y b.

    param int a cualquier entero
    param int b cualquier entero
    returns la sumatoria de a y b    
    """

    total = a + b
    return total