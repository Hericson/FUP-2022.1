import math

def cria_ponto(valor_x, valor_y):
    return {'x': valor_x, 'y': valor_y}

def calcula_distancia(ponto_1, ponto_2):
    return ((ponto_1['x'] - ponto_2['x']) ** 2 + (ponto_1['y'] - ponto_2['y']) **2 ) ** 0.5

def cria_circulo(ponto_1, ponto_2):
    return {'centro': ponto_1, 'raio': calcula_distancia(ponto_1, ponto_2)}

def calcula_comprimento_circulo(circulo):
    return 2 * math.pi * circulo['raio']

def converte_vetor(vetor):
    for i in range(len(vetor)):
        vetor[i] = float(vetor[i])
    return vetor

ponto_1 = converte_vetor(input("Digite as coordenadas do primeiro ponto (x,y): ").split(','))
ponto_2 = converte_vetor(input("Digite as coordenadas do segundo ponto (x,y): ").split(','))

ponto_1_dict = cria_ponto(ponto_1[0], ponto_1[1])
ponto_2_dict = cria_ponto(ponto_2[0], ponto_2[1])

circulo = cria_circulo(ponto_1_dict, ponto_2_dict)
print(f"ponto 1: ({ponto_1_dict['x']}, {ponto_1_dict['y']})")
print(f"ponto 2: ({ponto_2_dict['x']}, {ponto_2_dict['y']})")
print(f'Comprimento do circulo: {calcula_comprimento_circulo(circulo)}')