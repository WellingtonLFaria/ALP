divisiveis = 0
for c in range(1067, 3628):
    if c % 2 == 0 and c % 7 == 0:
        divisiveis += 1
print(divisiveis)
