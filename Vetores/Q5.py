# Problema 5

# Faça um Programa que leia dois vetores com 5 elementos cada. 
# Gere um terceiro vetor de 10 elementos, cujos valores deverão ser compostos pelos elementos 
# intercalados dos dois outros vetores.

vetor_1 = []
for i in range(5):
    vetor_1.append(int(input(f"Digite o {i+1}º elemento do vetor 1: ")))

vetor_2 = []
for i in range(5):
    vetor_2.append(int(input(f"Digite o {i+1}º elemento do vetor 2: ")))


vetor_resultante = []

for i in range(5):
    vetor_resultante.append(vetor_1[i])
    vetor_resultante.append(vetor_2[i])

print(f"Vetor 1: {vetor_1}")
print(f"Vetor 2: {vetor_2}")
print(f"Vetor Resultante: {vetor_resultante}")