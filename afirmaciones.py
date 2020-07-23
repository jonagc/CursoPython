"""
- Programacion defensiva
- Pueden utilizarce para verificar que los tipos sean correctos en una funcion
- Tambien sirven para debbugear

"""

# assert <expresion boolean>, <mensaje de error>

def letra_primera(lista_de_palabra):
    letra_primera = []

    for palabra in lista_de_palabra:
        assert type(palabra) == str, f'{palabra} no es str'
        assert len(palabra) > 0, f'No se permiten str vacios'

        letra_primera.append(palabra[0])

    return letra_primera
