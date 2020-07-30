
def fibonnacci(n):
    if n == 0 or n == 1:
        return 1
    
    return fibonnacci(n - 1) + fibonnacci(n - 2)

n = int(input('Ingresa un número: '))

print(fibonnacci(n))


def fibo(n):
    a=0
    b=1

    for i in range(n):
        c=a+b
        a=b
        b=c

    return b

if __name__ =='__main__':
    n = int(input('Ingresa un número: '))

    print(fibo(n))

