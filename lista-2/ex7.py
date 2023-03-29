area = float(input('Informe em m² o tamanho da área a ser pintada: '))

litros_necessarios = area/3
latas_necessarias = litros_necessarios/18

if latas_necessarias > int(latas_necessarias):
    latas_necessarias = latas_necessarias + ((int(latas_necessarias)+1)-latas_necessarias)

preco_total = latas_necessarias * 80

print('-'*50)
print(f'Área a ser pintada(m²): {area:.2f}\nLitros de tinta necessários: {litros_necessarios:.2f}\nLatas de tintas necessárias: {latas_necessarias:.2f}\nPreço Total a pagar: R$ {preco_total:.2f}')