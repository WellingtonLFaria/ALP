valor = int(input('Informe um valor para a seu respectivo número da sequencia de Fibonacci: '))
sequencia = [1, 1]

while len(sequencia)<valor:
    prox_valor = sequencia[-1] + sequencia[-2]
    sequencia.append(prox_valor)

for n in sequencia:
    print(f'{n}', end='  ')

print(f'\nO valor que está posição {valor} informada é: {sequencia[-1]}')