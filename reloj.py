hora = 0
minutos = 0
segundos = 0

while hora < 24:
    while minutos <= 60:
        while segundos <= 60:
            print(hora, ':', minutos, ':', segundos)
            segundos += 1
        minutos += 1
        segundos = 0
    hora += 1
    minutos = 0
