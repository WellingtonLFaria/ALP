while True:
    valor_do_troco = int(input('Informe o valor do troco: '))
    notas = (50, 20, 10, 5, 2, 1)
    notas_utilizadas = []
    for nota in notas:
        if valor_do_troco // nota > 0:
            for c in range(0, valor_do_troco//nota):
                notas_utilizadas.append(nota)
            valor_do_troco -= (valor_do_troco//nota)*nota


    print(f'Notas necessárias para realizar o troco: {len(notas_utilizadas)}')

    for nota in notas:
        if nota in notas_utilizadas:
            print(f'Nota de R$ {nota:.2f}: {notas_utilizadas.count(nota)}')
    