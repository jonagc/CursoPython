def run():
    numero = int(input('Ingrese el número: '))
    if primo(numero):
        print('El número ' +str(numero) + ' ES primo')
    else:
        print('El número ' +str(numero) + ' NO es primo')


def primo(numero):
    if numero < 2:
        return False
    else:
        for i in range(2, numero):
            if numero % i == 0:
                return False
            else:
                continue
    return True


if __name__ == '__main__':
    run()