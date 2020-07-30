#Encontrar el primer caracter que no se repite

"""
"abacabad"  c
"abacabaabacaba" _
"abcdefghijklmnopqrstuvwxyziflskecznslkfabe" d
"bcccccccccccccyb" y

"""

def first_not_repeating_char(char_sequence):
    

    for letra in char_sequence:
        contador = 0
        for i in char_sequence:
            if letra == i:
                contador += 1
        if contador == 1:
            return letra
    return '_'


if __name__ == '__main__':
    char_sequence = str(input('Escribe una secuencia de caracteres: '))

    result = first_not_repeating_char(char_sequence)

    if result == '_':
        print('Todos los caracteres se repiten.')
    else:
        print(f'El primer caracter no repetido es: {result}')
