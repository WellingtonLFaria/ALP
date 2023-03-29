from random import sample

def intercalar_valores():
    vetor1 = sample(range(1, 100), 10)
    vetor2 = sample(range(1, 100), 10)
    vetor3 = []

    for c in range(0, 10):
        vetor3.append(vetor1[c])
        vetor3.append(vetor2[c])
    
    return vetor1, vetor2, vetor3

vetor1, vetor2, vetor3 = intercalar_valores()
print(f'Vetor 1: {vetor1}\nVetor 2: {vetor2}\nVetor 3: {vetor3}')
