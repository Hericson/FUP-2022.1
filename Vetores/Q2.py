import os
os.system('cls' if os.name == 'nt' else 'clear')

# Problema 2

# Faça um programa que preencha dois vetores, X e Y, com 5 números inteiros cada. Calcule e mostre um vetor resultante contendo a Interseção entre X e Y (apenas os elementos que aparecem nos dois vetores, sem repetições).

X = []
#Popular o vetor X
for i in range(5):
    X.append(int(input(f"Digite o {i+1}º número do vetor X: ")))

Y = []
print()

#Popular o vetor Y
for i in range(5):
    Y.append(int(input(f"Digite o {i+1}º número do vetor Y: ")))

vetor_comum = []

for n in X:
    if n in Y and n not in vetor_comum:
        vetor_comum.append(n)

print(f"Vetor resultante: {vetor_comum}")
        

