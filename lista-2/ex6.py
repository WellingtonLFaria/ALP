ganho_por_hora = float(input('Informe o valor ganho por hora trabalhada: '))
horas_trabalhadas = float(input('Informe a quantidade de horas trabalhadas no mês: '))

salario_bruto = ganho_por_hora * horas_trabalhadas
imposto_de_renda = salario_bruto * (18/100)
inss = salario_bruto * (8/100)
sindicato = salario_bruto * (5/100)
salario_liquido = salario_bruto - (imposto_de_renda + inss + sindicato)

print('-'*30)
print(f'Salário Bruto: R$ {salario_bruto:.2f}')
print('-'*30)
print('DESCONTOS')
print(f'Imposto de Renda: R$ -{imposto_de_renda:.2f}\nINSS: R$ -{inss:.2f}\nSindicato: R$ -{sindicato:.2f}')
print('-'*30)
print(f'Salário Líquido: R$ {salario_liquido:.2f}')
