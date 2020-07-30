'''
Un decorador es una funcion que recibe como parametro a otra funcion y modifica su comportamiento.
Un decorador se aplica a una funcion o metrodo con el simbolo @.
Super util para definir su una funcion debe ejecutarse o no:
    Por ejemplo, en servidores web, existen ciertas fucniones que anda mas debn ejecutarse si un usuario se encuentra autenticado.
'''
def protected(func):

    def wrapper(password):

        if password == 'platzi':
            return func()
        else:
            print('La constraseña es incorrecta!')

    return wrapper #sin los parentesis para que no se ejhecute la funcion

@protected
def protected_func():
    print('Tu contraseña es correcta.')


if __name__ == '__main__':
    password = str(input('Ingresa tu contraseña: '))

    
    protected_func(password)