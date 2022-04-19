import os
os.system('cls' if os.name == 'nt' else 'clear')

# Problema 4

# Faça um programa que receba um número inteiro positivo e indique se ele é primo.

x = int(input("Digite um número inteiro positivo: "))

if x > 1:
    for i in range(2, x):
        if x % i == 0:
            print(x, "não é primo")
            break
    else:
        print("é primo")
else:
    print(x, "não é primo")


    
        
    

