while True:
    resto_0_ocasioes = 0
    n = int(input('Informe um valor para saber se ele é primo: '))
    for c in range(0, n):
        if n % (c+1) == 0:
            resto_0_ocasioes += 1
    if resto_0_ocasioes == 2:
        print(f'O número {n} é primo!')
        print('-'*40)
    else:
        print(f'O número {n} não é primo!')
        print('-'*40)