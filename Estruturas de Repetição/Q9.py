# Problema 9

# Faça um programa que gere e escreva os 4 primeiros números perfeitos. Um número perfeito é todo inteiro positivo que seja igual à soma de seus divisores. (Ex.: 6 = 1 + 2 + 3; 28 = 1 + 2 + 4 + 7 + 14, etc.)

import os
os.system('cls' if os.name == 'nt' else 'clear')
cont = 0
for x in range(1, 10**6):
    soma = 0
    for div in range(1,x):
        if x % div == 0:
            soma += div
    if soma == x:
        print(f"{x} é perfeito")
        cont += 1

        if cont == 4:
            break
    

