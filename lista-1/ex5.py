valor_do_produto = float(input('Informe o valor do produto(R$): '))
porcentagem_do_desconto = float(input('Informe o percentual de desconto: '))

valor_do_desconto = valor_do_produto * (porcentagem_do_desconto/100)
valor_do_produto = valor_do_produto - valor_do_desconto

print(f'O valor do produto após o desconto de R${valor_do_desconto:.2f} é de: R${valor_do_produto:.2f}')