"""
Algoritmo que recorre repetidamente una lista que necesita ordenarse. Compara elementos adyacentes 
y los intercambia si estan en el orden incorrecto. 
Este procedimiento se repite hasta que no se requiere mas intercambios, lo que indica que la lsita se encuentra ordenada.
"""

import random

def ordenamiento_burbuja(lista):
    n = len(lista)

    for i in range(n):
        for j in range(0, n - i - 1):
            
            if lista[j] > lista [j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista

if __name__ == '__main__':

    tamano_lista = int(input('De que tamaño será la lista: '))

    lista = [random.randint(0, 100) for i in range(tamano_lista)]
    print(lista)

    lista_ordenada = ordenamiento_burbuja(lista)
    print(lista_ordenada)