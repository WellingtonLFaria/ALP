palavra = str(input('Digite uma palavra: '))
isograma = True

palavrawspec = palavra.replace(' ', '')
palavrawspec = palavrawspec.replace('-', '')
palavrawspec = palavrawspec.replace('_', '')

for letra in palavrawspec:
    if palavrawspec.count(letra) > 1:
        isograma = False

if isograma == True:
    print(f'A palavra {palavra} é um isograma')
elif isograma == False:
    print(f'A palavra {palavra} não é um isograma')