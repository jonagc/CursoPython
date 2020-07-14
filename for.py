def run():
    # nombre = input('Escribe tu nombre: ')
    # for letra in nombre:
    #     print(letra)

    # frase = input('Escribe una frase: ')
    # for caracter in frase:
    #     print(caracter.upper())

    # for contador in range(1000):
    #     if contador % 2 != 0:
    #         continue
    #     print(contador)

    # for i in  range(10000):
    #     print(i)
    #     if i == 5678:
    #         break
    text = input('Escribe un texto: ')
    for i in text:
        if i == 'o':
            break
        print(i) 


if __name__ == '__main__':
    run()