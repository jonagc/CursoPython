# -*- cooding: utf-8 -*-



KEYS = {
    'a': 'w',
    'b': 'E',
    'c': 'x',
    'd': '1',
    'e': 'a',
    'f': 't',
    'g': '0',
    'h': 'C',
    'i': 'b',
    'j': '!',
    'k': 'z',
    'l': '8',
    'm': 'M',
    'n': 'I',
    'o': 'd',
    'p': '.',
    'q': 'U',
    'r': 'Y',
    's': 'i',
    't': '3',
    'u': ',',
    'v': 'J',
    'w': 'N',
    'x': 'f',
    'y': 'm',
    'z': 'W',
    'A': 'G',
    'B': 'S',
    'C': 'j',
    'D': 'n',
    'E': 's',
    'F': 'Q',
    'G': 'o',
    'H': 'e',
    'I': 'u',
    'J': 'g',
    'K': '2',
    'L': '9',
    'M': 'A',
    'N': '5',
    'O': '4',
    'P': '?',
    'Q': 'c',
    'R': 'r',
    'S': 'O',
    'T': 'P',
    'U': 'h',
    'V': '6',
    'W': 'q',
    'X': 'H',
    'Y': 'R',
    'Z': 'l',
    '0': 'k',
    '1': '7',
    '2': 'X',
    '3': 'L',
    '4': 'p',
    '5': 'v',
    '6': 'T',
    '7': 'V',
    '8': 'y',
    '9': 'K',
    '.': 'Z',
    ',': 'D',
    '?': 'F',
    '!': 'B',
    ' ': ' ',
}


def crypher(message):
    message_crypher = ''
    for letra in message:
        message_crypher += (KEYS[letra])
    
    return message_crypher

def decipher(message):
    message_decipher = ''

    for valor in message:
        for key, value in KEYS.items():
            if value == valor:
                message_decipher +=  key
                break
    return message_decipher


def run():

    command = str(input('''--- * --- * --- * --- * --- * --- * --- * --- * --- * --- * --- * --- * ---

    Bienvendios a criptogrfía. ¿Qué deseas hacer?

        [c]ifrar mensaje
        [d]ecifrar mensaje
        [s]alir       
    '''))

    if command == 'c':
        message = str(input('Escribe el mensaje: '))
        message_crypher = crypher(message)
        print(message_crypher)

    elif command == 'd':
        message = str(input('Escribe el mensaje cifrado: '))
        message_encrypher = decipher(message)
        print(message_encrypher)

    elif command == 's':
        print('Hasta pronto!!')
        exit
    else:
        print('La opción ingresada es invalida. Por favor, ingresala nuevamente: ')
        print('')
        return run()


if __name__ == '__main__':
    print('                 M E N S A J E S  C I F R A D O S')
    print('')
    run()

