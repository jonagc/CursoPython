'''
- Comparar la eficiencia de un algoritmo 

- Complejidad temporal vs complejidad espacial

- Podemos definirla como T(n)

Como se usaria:
 - Cronometrar el tiempo en que corre un algoritmo
 - Contar los pasos con una medida ebstracta de operacion
 - Contar los pasos conforme nos aproximamos al infinito

'''

import time
import sys

sys.setrecursionlimit(1000000)


def factorial(n):
    respuesta = 1

    while n > 1:
        respuesta *= n
        n -= 1

    return respuesta

def factorial_r(n):
    if n == 1:
        return 1

    return n * factorial_r(n - 1)

if __name__ == '__main__':
    n = 1000


    comienzo = time.time()
    factorial(n)
    final = time.time()
    print(final - comienzo)

    comienzo = time.time()
    factorial_r(n)
    final = time.time()
    print(final - comienzo)


