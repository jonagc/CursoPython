#Para abrir el archivo se ocupa la funcion open. Recibe dos parametros, donde se encuentra el archivo y el modo el como se quiere operar el archivo

"""
r = read
w = write
a = append
r+ = read and write

se debe cerrar el archivo con el metodo close

La mejor manera de abrir archivos es con el keyword with

sintaxis:

with open('file.txt', 'r') as f:
    for i in range(5):
        print('Hello')
"""



def run():
    counter = 0
    with open('aleph.txt', encoding='utf-8') as f:
        #print(f.readlines()) #separa cada salto de linea como un ppedazo de string y lo imprime

        for line in f:
            counter += line.count('Beatriz') #Cuenta cantidad de veces que aparece la palabra Beatriz dentro de cada pedazo de string

    print(f'Beatriz se encuentra {counter}')


if __name__ == '__main__':
    run()