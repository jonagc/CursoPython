
def suma(tipo_peso, valor_dolar):
    pesos = input('Cuántos pesos ' + tipo_peso + ' tienes?: ')
    pesos = float(pesos)
    dolares = pesos/valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print('Tienes $' + dolares + ' dólares')

menu = """
Bienvenidos al conversor de monedas 💰💰

1 - Pesos colombianos
2 - Pesos argentinos
3 - Pesos mexicanos

Elige una opción: """

opcion = int(input(menu))

if opcion == 1:
    suma('colombianos', 3875)
elif opcion == 2:
    suma('argentino', 65)
elif opcion == 3:
    suma('mexicanos', 24)
else:
    print('INGRESA UNA OPCIÓN VALIDA')