while True:
    print('-'*40)
    try:
        valor = float(input('Digite um número entre 0 e 10: '))
        if valor > 10 or valor < 0:
            print('Por favor informe um valor entre 0 e 10!')
        else:
            break
    except ValueError:
        print('Por favor informe um valor válido!')

# Usei print para não ficar somente um encerramento sem feedback 
print('Valor armazenado!')
