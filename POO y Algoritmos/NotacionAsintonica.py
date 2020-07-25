"""
No importa las variaciones pequeñas.
Se centra en el enfoque conforme al tamñao del prblema se acerca al inifinito.
MEjor de los casos, promedio, peor de los casos.
Big O Notation
Nada mas importa el termino con mayor tamaño.
"""

#Ley de la suma -> Crecimiento lineal
def f(n):

    for i in range(n):
        print(i)

     for i in range(n):
        print(i)
#O(n) + O(n) = O(n+n) = O(2n) = O(n)

#Ley de la suma -> Crecimiento cuadratico

def f(n):

    for i in range(n):

        for j in range(n):
            print(i, j)

#O(n) * O(n) = O(n*n) = O(n**2)

#Recursividad multiple -> Crecimiento exponencial

def fibonnacci(n):

    if n == 0 or n == 1:
        return 1
    return fibonnacci(n-1) + fibonnacci(n-2)

#O(2**n)


