import random

def generar_contrasena():
    mayusculas = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
    minusculas = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    simbolos = ['!', '#', '$', '&', ' /', '(', ')']
    numeros = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0' ]

    caracteres = mayusculas + minusculas + simbolos + numeros

    contrasena = []

    for i in range(10):
        caracter_ramdom = random.choice(caracteres)
        contrasena.append(caracter_ramdom)

    contrasena = "".join(contrasena) #vuelve los datos una linea
    return contrasena

def run():
    contrasena = generar_contrasena()
    print('Tu nueva contraseña es: ' + contrasena)

if __name__ == '__main__':
    run()