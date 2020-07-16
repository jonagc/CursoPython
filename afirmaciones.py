"""
- Programacion defensiva
- Pueden utilizarce para verificar que los tipos sean correctos en una funcion
- Tambien sirven para debbugear

"""

# assert <expresion boolean>, <mensaje de error>

def primera_letra(lista_de_palabra):
    primeras_letras = []

    for palabra in lista_de_palabra:
        assert type(palabra) == str, f'{palabra} no es str'
        assert len(palabra) > 0, f'No se permiten str vacios'

        primeras_letras.append(palabra[0])

    return primeras_letras