# Problema 5

# Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).

# Dica: 1 byte = 8 bits, 1 MB = $10^6$ bytes, 1 Mbps = $10^6$ bits por segundo.

nome_arquivo = input("Qual o nome do arquivo? ")
tamanho_arquivo = float(input("Qual o tamanho do arquivo para Download (em MB): "))
velocidade_link = float(input("Qual a valocidade do link de internet (Em Mbps): "))

tempo_minutos = ((tamanho_arquivo * 8) / velocidade_link) / 60

print("O arquivo", nome_arquivo,
     "será baixado em", round(tempo_minutos, 2), "minutos")