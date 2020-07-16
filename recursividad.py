#Algoritmica
"""Una forma de crear soluciones utiulizando el principio de divide y vencerás"""

#Programatica
"""Una técnica programatica mediante la cual una funcion se llama a si misma """ 

# Factoriales

def factorial(n):
    """Calcula el factorial de n.

    n int > 0
    return n!
    """
    if n == 1:
        return 1
    
    return n * factorial(n - 1)

n = int(input('Escribe un entero: '))

print(factorial(n))

""" Python tiene como limite de recursividad 1000, por lo que si se quiere cambiar se puede importar 

import sys

sys.setrecursionlimit(2000)

"""