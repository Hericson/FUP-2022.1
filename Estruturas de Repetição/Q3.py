import os
os.system('cls' if os.name == 'nt' else 'clear')

# Problema 3

# Faça um programa que possa calcular o fatorial de vários números em uma mesma execução. O usuário deve digitar um número menor ou igual a zero para interromper a execução.

# Exemplos de execução:

# Digite um número inteiro positivo: 4

# Fatorial de 4: 24

# Digite um número inteiro positivo: 5

# Fatorial de 5: 120

# Digite um número inteiro positivo: 0

# Fim.


while True:
    x = int(input("Digite um número inteiro positivo: "))

    if x <=0:
        print("Fim")
        break
    
    ##Calcular o fatorial
    fatorial = x 
    for i in range(2, x):
        fatorial *= i

    print("Fatorial de", x, ":", fatorial)
