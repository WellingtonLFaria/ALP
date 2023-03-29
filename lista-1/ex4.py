salario = float(input('Informe seu salário(R$): '))
porcentagem = float(input('Informe a porcentagem do aumento: '))

aumento = salario * (porcentagem/100)

salario = salario + aumento

print(f'Seu novo salário após o aumento de R${aumento:.2f} é de: R${salario:.2f}')