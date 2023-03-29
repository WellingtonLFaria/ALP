n1 = float(input('Número 1: '))
n2 = float(input('Número 2: '))
n3 = float(input('Número 3: '))

if n1 == n2 == n3:
    print('Todos os números são iguais!')
else:
    if n1 >= n2 and n1 >= n3:
        print(f'{n1} é o maior número.')
    elif n2 >= n1 and n2 >= n3:
        print(f'{n2} é o maior número.')
    elif n3 >= n1 and n3 >= n2:
        print(f'{n3} é o maior número.')
