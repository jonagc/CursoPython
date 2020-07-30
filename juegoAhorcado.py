# -*- coding: utf-8 -*-
import random

IMAGENS= ['''

    +---+
        |
        |
        |
        |
        |
        ========''', '''


    +---+
    |   |
        |
        |
        |
        |
        ========''', '''


    +---+
    |   |
    0   |
        |
        |
        |
        ========''', '''


     +---+
     |   |
     0   |
     |   |
         |
         |
         ========''', '''


     +---+
     |   |
     0   |
    /|   |
         |
         |
         ========''', '''    


      +---+
     |   |
     0   |
    /|\  |
         |
         |
         ========''', '''      


     +---+
     |   |
     0   |
    /|\  |
    /    |
         |
         ========''', '''     


     +---+
     |   |
     0   |
    /|\  |
    / \  |
         |
         ========''']

WORDS = [
    'lavadora',
    'Secadora',
    'sofa',
    'gobierno',
    'democracia',
    'computadora',
    'teclado'
    ]
def random_word():
    idx = random.randint(0, len(WORDS) - 1)
    return WORDS[idx]

def display_board(hidden_word, tries):
    print(IMAGENS[tries])
    print('')
    print(hidden_word)
    print('--- * --- * --- * --- * --- * --- * --- * --- * --- * ---')
    
def run():
    word = random_word()
    hidden_word = ['-'] * len(word)
    tries = 0
    
    while True:
        display_board(hidden_word, tries)
        current_letter = str(input('Escoge una letra: '))

        letter_indexes = []
        for i in range(len(word)):
            if word[i] == current_letter:
                letter_indexes.append(i)

        if len(letter_indexes) == 0:
            tries += 1
            if tries == 7:
                display_board(hidden_word, tries)
                print('')
                print(f'¡Perdiste! La Palabra correcta era {word}')
                break
        else:
            for i in letter_indexes:
                hidden_word[i] = current_letter

            letter_indexes = []
        try:
            hidden_word.index('-')
        except ValueError:
            print('')
            print(f'¡Felicidades! GANASTE. La palabra es: {word}' )
            break

if __name__ == '__main__':
    print('BIENVENIDOS A AHORCADOS')
    run()
