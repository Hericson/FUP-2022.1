# Problema 4

# Faça um programa que calcule e escreva o valor do número $\pi$ com precisão de 0,00001 usando a série abaixo:

# pi = 4/1 - 4/3 + 4/5 - 4/7 + 4/9 - 4/11 + ...

import os
os.system('cls' if os.name == 'nt' else 'clear')

import math

pi = 4
den = 1
flag = True

while abs(pi - math.pi) > 10 ** -5:
    den += 2

    if flag == True:
        flag = False
        pi -= 4/den
    else:
        flag = True
        pi += 4/den

print(f"Pi Verdadeiro = {math.pi:.5f}")
print(f"Pi Calculado = {pi:.5f}")

    
    

