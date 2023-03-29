a = int(input("Digite o número a: "))
b = int(input("Digite o número b:: "))

anterior = a
atual = b

resto = atual % anterior
while resto != 0:
    resto = anterior % atual
    anterior = atual
    atual = resto

print(f"Máximo Divisor Comum: {anterior}")