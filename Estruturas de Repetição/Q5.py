# Problema 5

# Faça um programa que receba 5 números inteiros, calcule e mostre a soma dos números pares e a soma dos números primos. Faça um teste para esse programa considerando os valores de entrada 9, 1, 2, 19, 18.

#Apenas pra limpar o terminal quando executa
import os
os.system('cls' if os.name == 'nt' else 'clear')

soma_pares = 0
soma_primos = 0

for i in range(5):
    x = int(input("Digite um número inteiro positivo: "))
    ## Somar os números pares
    if x % 2 == 0:
        #soma_pares = soma_pares + x
        soma_pares += x
    ## Somar os números primos
    for j in range(2,x):
        if x % j == 0:
            break
    else:
        if x != 1:
            soma_primos += x

print("Soma dos números pares: ", soma_pares)
print("Soma dos números primos: ", soma_primos)
        
        