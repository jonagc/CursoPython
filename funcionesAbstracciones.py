

def exhaustiva(objetivo):
    respuesta = 0

    while respuesta**2 < objetivo:
        respuesta += 1

    if respuesta**2 == objetivo:
        print(f'La raiz cuadrada de {objetivo} es igual a {respuesta}')
    else:
        print(f'El número {objetivo} no posee raiz cuadrada exacta')

def aproximacion(objetivo):
    epsilon = 0.01
    respuesta = 0.0
    paso = epsilon**2

    while abs(respuesta**2 - objetivo) >= epsilon and respuesta <= objetivo:
        respuesta += paso

    if abs(respuesta**2 - objetivo) >= epsilon:
        print(f'No se encontró la raiz cuadrada de {objetivo}')
    else:
        print(f'La raiz cuadrada aproximada de {objetivo} es {respuesta}')


def binaria(objetivo):
    epsilon = 0.01
    bajo = 0.0
    alto = max(1.0, objetivo)
    respuesta = (alto + bajo) / 2

    while abs(respuesta**2 - objetivo) >= epsilon:
        if respuesta**2 < objetivo:
            bajo = respuesta
        else:
            alto = respuesta
        
        respuesta = (alto + bajo) / 2

    print(f'La raiz cuadrada de {objetivo} es {respuesta}')

def opciones():
    opciones = int(input("""
    1.- Busqueda exhaustiva
    2.- Busqueda aproximada
    3.- Busqueda binaria

    Ingrese el metodo a usar:
    """))

    if opciones != 1 or 2 or 3:
        print('Ingrese una opción valida!!')
        
    else:
        objetivo = int(input('Ingrese el número: '))

        if opciones == 1:
            exhaustiva(objetivo)
        elif opciones == 2:
            aproximacion(objetivo)
        elif opciones == 3:
            binaria(objetivo)
    
        


if __name__ == "__main__":
    opciones()
