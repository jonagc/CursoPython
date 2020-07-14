def run():
    direccion = input('Escribe una dirección: ')
    for i in direccion:
        if i in ('0','1','2','3','4','5','6','7','8','9'):
            break
        elif i == '#':
            continue
        else:
            print(i)


if __name__ == '__main__':
    run()