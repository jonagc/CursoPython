menu = """
Bienvenidos al conversor de monedas 💰💰

1 - Pesos colombianos
2 - Pesos argentinos
3 - Pesos mexicanos

Elige una opción: """

opcion = int(input(menu))

def convertidor(valor_dolar, pesos):
    pesos = float(pesos)
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes $" + dolares + " dólares")

def saludo(opcion):
    print("""   
    Hola 
    ¿Cómo estás?
    Eligiste la opción: """ + str(opcion))


if opcion == 1:
    saludo(opcion)
    pesos = input("\n¿Cuántos pesos colombianos tienes?: ")
    valor_dolar = 3875
    convertidor(valor_dolar, pesos)
elif opcion ==2:
    saludo(opcion)
    pesos = input("\n¿Cuántos pesos argentinos tienes?: ")
    valor_dolar = 65
    convertidor(valor_dolar, pesos)
elif opcion == 3:
    saludo(opcion)
    pesos = input("\n¿Cuántos pesos mexicano tienes?: ")
    valor_dolar = 24
    convertidor(valor_dolar, pesos)
else:
    print('Ingrese una opción correcta')
