# extiende la lista con valores dentro de un iterable como un range()
lista.extend(iterable)
# Agrega un valor en la posición i y recorre todos los demás. No borra nada.
lista.insert(i, ‘valor’)
lista.pop(i)  # Elimina valor en la posición i de la lista.
lista.remove(‘valor’)  # Elimina el primer elemento con ese valor.
lista.clear()  # Borra elementos en la lista.
lista.index(‘valor’)  # Retorna posición del primer elemento con el valor.
# Retorna posición del elemento con el valor dentro de los elementos desde posición start hasta posición end)
lista.index(‘valor’, start, end)
lista.count(‘valor’)  # Cuenta cuántas veces esta ese valor en la lista.
lista.sort()  # Ordena los elementos de mayor a menor.
lista.sort(reverse=True)  # Ordena los elementos de menor a mayor.
lista.reverse()  # Invierte los elementos
lista.copy()  # Genera una copia de la lista. También útil para clonar listas.


#Si tengo una lista y la asigno a otra, sigue siendo la misma lista. Si veo el id de cada una apuntan a la misma memoria, por
#por tanto, si edito una la otra igualmente se editará

lista = [1,2,3]
lista2 = lista #mismos numeros  y apuntan a la msima memoria, osea son la misma lista

#Si quiero clonar una lista se puede hacer con el metodo de list
lista2 = list(lista) #Ahora tienen los mismos valores, pero si edito una, solo se editara esa y la otra queda con los valores que le corresponde
#Se recomienda clonar lista para evitar errores.

#list comprehension
lista = list(range(100)) #Crear una lista de 0 a 99

double = [i * 2 for i in lista] #Crea una lista 'double' multiplicacndo por 2 cada elemento de la lista 'lista'

pares = [i for i in lista if i % 2] #colocar elemento en la lista 'pares' por cada elemento dentro de la lista 'lista' que sea par
#donde i son los elementos, for pasa por cada uno de ellos, y la condicional que vea que son pares.