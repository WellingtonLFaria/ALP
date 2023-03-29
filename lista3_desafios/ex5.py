while True:
    numero = int(input('\nInforme um número: '))

    numerostr = str(numero)

    elementos = []
    for elemento in numerostr:
        elementos.append(elemento)

    elementoscontrario = []
    for c in range(len(numerostr)-1, -1, -1):
        print(numerostr[c], end='')
