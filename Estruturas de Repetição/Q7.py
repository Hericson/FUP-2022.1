# Problema 7

# Considere um tabuleiro de xadrez comum, com 64 casas. Qual o total em toneladas (1t = 1000kg) que será obtido se você colocar na primeira casa 1 grão de trigo, na segunda casa, 2 grãos de trigo, na terceira casa, 4 grãos de trigo, e assim sucessivamente, sempre dobrando a quantidade anterior. Sabe-se que 1 grão de trigo pesa 0,00526g. Escreva um programa para realizar esse cálculo.

#Apenas pra limpar o terminal quando executa
import os
os.system('cls' if os.name == 'nt' else 'clear')

peso_grao = 0.00526

adicionados = 1
quantidade_graos = adicionados

for casa in range(63):
    adicionados = 2 * adicionados
    quantidade_graos += adicionados

peso_total = (quantidade_graos * peso_grao) / (10 ** 6)

print("Você terá", quantidade_graos, "grãos que pesam", peso_total, "toneladas")
print(f"Você terá {quantidade_graos:.2e}, grãos que pesam {peso_total:.2e} toneladas")
