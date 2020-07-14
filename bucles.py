def run():
    i = 0
    potencia = 2
    while potencia <= 1000000:
        potencia = 2**i
        print('2 elevado a ' +str(i) + ' es igual a: ' +str(potencia))
        i +=1
       

if __name__ == '__main__':
    run()
