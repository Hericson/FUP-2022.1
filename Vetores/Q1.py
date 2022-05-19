import os
os.system('cls' if os.name == 'nt' else 'clear')

# Problema 1

# Faça um programa que receba cinco números e mostre a saı́da a seguir:

# Digite o 1º número: 5
# Digite o 2º número: 3
# Digite o 3º número: 2
# Digite o 4º número: 0
# Digite o 5º número: 2

# O menor número digitado foi: 0

# O maior número digitado foi: 5

# A soma dos números digitados foi: 5 + 3 + 2 + 0 + 2 = 12

numeros = []
menor = 0
maior = 0
soma = 0

for i in range(5):
    valor = int(input(f"Digite o {i+1}º número: "))
    numeros.append(valor)

    #Verificar qual o menor valor
    if numeros[-1] < menor or i == 0:
        menor = numeros[-1]

    #Verificar o maior
    if numeros[-1] > maior or i == 0:
        maior = numeros[-1]

    #Realizar a soma
    soma += numeros[-1]

print(f"O menor número digitado foi: {menor}")
print(f"O maior número digitado foi: {maior}")

print(f"A soma dos números digitados foi: ", end="")

for i in range(4):
    print(f"{numeros[i]} + ", end="")
print(f"{numeros[-1]} = {soma}")
        
    

    



