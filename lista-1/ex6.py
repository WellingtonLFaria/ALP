distância_a_percorrer = float(input('Informe a distância total em a percorrer(km): '))
velocidade_media = float(input('Informe a velocidade média durante o percurso(km/h): '))

tempo_estimado_de_viagem = distância_a_percorrer/velocidade_media

print(f'Para a viagem de {int(distância_a_percorrer)}km, em uma velocidade de {int(velocidade_media)}km/h será gasto {tempo_estimado_de_viagem} horas.')