import random

def busquerda_binaria(lista_numero, numero_buscado, comienzo, final):

    mitad = (comienzo + final) // 2


    if comienzo > final:
        return False
    
    if numero_buscado == lista_numero[mitad]:
        return True
    elif numero_buscado > lista_numero[mitad]:
        return busquerda_binaria(lista_numero, numero_buscado, mitad + 1, final)
    else:
        return busquerda_binaria(lista_numero, numero_buscado, comienzo, mitad - 1)


if __name__ == '__main__':

    lista_numero = sorted([random.randint(0, 100) for i in range(20)])

    
    print(lista_numero)

    numero_buscado = int(input('Ingrese el número a buscar: '))

    resultado = busquerda_binaria(lista_numero, numero_buscado, 0, len(lista_numero) - 1)
    
    if resultado:
        print(f'El número {numero_buscado} sí se encuentra en la lista')
    else:
        print(f'El número {numero_buscado} NO está en la lista')
    


