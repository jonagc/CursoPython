import random

def run():
    adivina = random.randint(1, 100)
    numero = int(input('Ingresa un número: '))

    while numero != adivina:
        if numero < adivina:
            print('El número es mayor. Prueba de nuevo!!\n')
        else:
            print('El número es menor. Prueba de nuevo!!\n')
        numero = int(input('Ingresa otro número: '))
    print('\nG A N A S T E!!\n')


if __name__ == '__main__':
    run()