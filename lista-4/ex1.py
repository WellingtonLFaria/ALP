from random import sample

def maior_e_menor(vetor):
    maior = vetor[0]
    menor = vetor[0]

    for numero in vetor:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero

    return vetor, maior, menor

numeros, maior, menor = maior_e_menor(sample(range(1, 100), 10))

print(f'Números: {numeros}\nMaior: {maior}\nMenor: {menor}')
