#Busca todos los elmentos de fomra secuencial

import random

def busqueda_lineal(lista, objetivo):

    match = False

    for elemento in lista:
        if elemento == objetivo:
            match = True
            break
        return match

if __name__ == '__main__':

    tamano_lista = int(input('De que tamaño quieres las lista: '))

    objetivo = int(input('Que numero quieres encontrar: '))

    lista = [random.randint(0, 100) for i in range(tamano_lista)]

    encontrado = busqueda_lineal(lista, objetivo)

    print(lista)
    print(f'El elemento {objetivo} {"esta" if encontrado else "no esta"} en la lista') #operadores ternarios, se puede colocar if en una linea de codigo
    