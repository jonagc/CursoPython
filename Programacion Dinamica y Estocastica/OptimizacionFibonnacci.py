#Numero de Fibonnacci

#Fn = Fn-1 + Fn-2

def fibonnacci_recursivo(n, l ='Izq'):
    print(n, l)
    if n == 0 or n == 1:
        return 1

    
    return fibonnacci_recursivo(n-1, l= 'Izq') + fibonnacci_recursivo (n-2, l= 'der')

def fibonnacci_dinamico(n, memo = {}, l='iz'):
    print(n, l)
    if n == 0 or n == 1:
        return 1
   
    try:
        return memo[n]
    except KeyError:
        resultado = fibonnacci_dinamico(n - 1, memo, l='iz') + fibonnacci_dinamico(n - 2, memo, l='de')
        
        memo[n] = resultado

        return resultado

if __name__ == '__main__':
    n = int(input('Escoge un numero: '))

    resultado = fibonnacci_dinamico(n)
    #resultado = fibonnacci_recursivo(n)
    print(resultado)

"""
     Recursividad sin memoria pasa por todos estos pasos
     Con memoria guarda aquellos que calcula y devuelve el resultado almacenado en memo[n], sin tener que
     realizar el calculo de fibonnacci de nuevo (f(2), f(3) en la sucesion de 5)
     
                                                15f(5)
                        1f(4)                     +                         10f(3)
             2f(3)         +      7f(2)                             11f(2)      +      14f(1)
      3f(2)     +    6f(1)    8f(1)   +    9f(0)             12f(1)    +     13f(0)
4f(1)    +    5f(0)



"""