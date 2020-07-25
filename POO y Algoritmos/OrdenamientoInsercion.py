import random


def insercion(lista):

    for i in range(1, len(lista)):
        valor_actual = lista[i]
        posicion_actual = i

        while posicion_actual > 0 and lista[posicion_actual - 1] > valor_actual:
            lista[posicion_actual] = lista[posicion_actual - 1]
            posicion_actual -= 1
            print(lista)
            
        lista[posicion_actual] = valor_actual
        print(lista)

    return lista

if __name__ == '__main__':

    tamano_lista = int(input('Ingrese el tamño de la lista: '))

    lista = [random.randint(0, 100) for i in range(tamano_lista)]

    print(lista)
    print(insercion(lista))

    

