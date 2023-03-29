from time import sleep

habitantesA = 80000
taxa_crescimentoA = 3

habitantesB = 200000
taxa_crescimentoB = 1.5

anos = 0

while habitantesA < habitantesB:
    habitantesA += (habitantesA*(taxa_crescimentoA/100))
    habitantesB += (habitantesB*(taxa_crescimentoB/100))
    anos += 1
    print('='*40)
    print(f'Habitantes A: {int(habitantesA)}\nHabitantes B: {int(habitantesB)}\nAnos passados: {anos}')
    
    # Usei sleep para ter uma melhor visualização do crescimento populacional
    sleep(0.5)

print('='*40)
print('Resultado Final:')
print(f'Habitantes A: {int(habitantesA)}\nHabitantes B: {int(habitantesB)}\nAnos passados: {anos} anos')