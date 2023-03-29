km_percorrido = float(input('Informe a quantidade de km percorridos pelo carro alugado: '))
dias_alugado = int(input('Informe por quantos dias o carro foi alugado: '))

preço_a_pagar = (60 * dias_alugado) + (0.15 * km_percorrido)

print(f'O preço total a pagar pelo carro alugado por {dias_alugado} dias e {km_percorrido} km rodado é de: R${preço_a_pagar:.2f}')