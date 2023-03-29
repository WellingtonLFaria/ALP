from random import sample

def pares_e_impares(vetor):
    pares = []
    impares = []

    for numero in vetor:
        if numero % 2 == 0:
            pares.append(numero)
        else:
            impares.append(numero)
    
    pares.sort()
    impares.sort()
    vetor.sort()
    return vetor, pares, impares
    
numeros, pares, impares = pares_e_impares(sample(range(1, 100), 20))

print(f'Números: {numeros}\nPares: {pares}\nÍmpares: {impares}')
