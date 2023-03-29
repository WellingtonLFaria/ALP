dias = int(input('Dia(s): '))
horas = int(input('Hora(s): '))
minutos = int(input('Minuto(s): '))
segundos = int(input('Segundo(s): '))

total_em_segundos = dias * 86400 + horas * 3600 + minutos * 60 + segundos

print(f'O total em segundos do tempo informado é: {total_em_segundos}')