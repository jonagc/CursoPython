# La funcion hash es un metodo para generear claves o llaves que representen de manera unicova para documentos o conjuntos de datos.

my_dicc = {
    'David' : 35,
    'Erika' : 32,
    'Jaime' : 50,

}

#my_dicc['David']
#Consulta de consola. Si no existe el valor entregue otro con metodo get
my_dicc.get('Juan', 30) #Como juan no existe en el diccionario consola me entregará el valor de 30

my_dicc.get('David', 30) # en este caso David si se encuentra en nuestro diccionario, por tanto me dará el valor 35

#cambiar o agregar llaves
my_dicc['Jaime'] = 20 #Esto cambia el valor de Jaime de 50 a 20

my_dicc['Pedro'] = 12 #Esto agregará a Pedro con su valor en el diccionario


#Borrar llaves
del my_dicc['Jaime'] #Borra a Jaime del diccionario

#Imprimir llaves
for llave in my_dicc.keys():
    print(llave)

#Imprimir valores
for valor in my_dicc.values():
    print(valor)

#Imprimir llaves y valores (items)
for items in my_dicc.items():
    print(items)

#Ver si existe una llave en el diccionario
'David' in my_dicc #Entrega booleano

def calificaciones():
    calificaciones = {}

    calificaciones['matematicas'] = 10
    calificaciones['algotimo'] = 9
    calificaciones['web'] = 9
    calificaciones['base_de_datos'] = 8

    for key, value in calificaciones.items():
        print('Llave: {}, valor: {}'.format(key, value))
        

    for key in calificaciones.keys():
        print('Asignaturas: {}'.format(key))

    for value in calificaciones.values():
        print('Notas: {}'.format(value))

if __name__ == '__main__':
    calificaciones()
