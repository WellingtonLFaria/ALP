cigarros_por_dia = int(input('Quantos cigarros você fuma por dia: '))
anos_fumando = int(input('Anos fumando: '))

total_de_minutos_perdidos = cigarros_por_dia * 365 * anos_fumando * 10
dias_perdidos = total_de_minutos_perdidos/1440

print(f'Você perdeu {dias_perdidos:.2f} dias de sua vida.')
