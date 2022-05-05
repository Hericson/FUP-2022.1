# Problema 11

# Faça um programa que aproxime a função exponencial com precisão de 0,00001 usando a série abaixo:

# e^x = x^0 + x¹ / 1! + x² / 2! + x³ / 3! + ...

import os
os.system('cls' if os.name == 'nt' else 'clear')

import math

x = float(input("Digite um número: "))

true_exp = math.exp(x)

exp = 1
cont = 0

while abs(exp - true_exp) > 10 ** -5:
    cont+=1
    den = cont
    ## Cálculo do Fatorial
    for i in range(2, cont):
        den *= i

    exp += (x ** cont) / den

print(f"exp({x}) verdadeiro = {true_exp:.6f}")
print(f"exp({x}) calculado = {exp:.6f}")
        

    

