peso = float(input('Informe o peso(kg): '))

print('-'*30)

if peso > 50:
    excesso = peso - 50
    multa = excesso * 4
    print(f'Peso dos peixes(kg): {peso:.2f}\nExcesso(kg): {excesso:.2f}\nMulta: R$ {multa:.2f}')
else:
    print(f'Peso dos peixes(kg): {peso:.2f}\nExcesso(kg): 0\nMulta: R$ 0')
