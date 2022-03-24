# Problema 1

# O circuito mundial de Fórmula 1 diz que um grande prêmio deve ter o percurso percorrido mı́nimo de 350 Km (Exceção de Mônaco). Faça uma programa que peça para o usuário fornecer o nome de um circuito e sua extensão. O programa deve fornecer como resposta o número de voltas necessários para que o circuito atenda a exigência da FIA. Exemplo:

# Nome do Circuito: Interlagos

# Extensão do Circuito (km): 4.309

# O circuito de Interlagos precisa de 82 voltas para completar 353.34 Km

import math

# Armazenar o nome do circuito
nome_circuito = input("Qual o nome do circuito? ")
# Armazenar a extensão do circuito
extensao_circuito = float(input("Qual a extensão do circuito? "))
# Armazenar o percurso mínimo
percurso_minimo = 350

numero_voltas = math.ceil(percurso_minimo / extensao_circuito)

extensao_corrida = numero_voltas * extensao_circuito

print("O circuito de", nome_circuito,
     "precisa de", numero_voltas,
     "voltas para completar",
     round(extensao_corrida, 2), "Km")


