import os
os.system('cls' if os.name == 'nt' else 'clear')

# Problema 1

# Faça um programa para calcular a área de um triângulo, recebendo a base e altura e que não permita a entrada de dados inválidos (valores menores ou iguais a 0).

while True:
    base = float(input("Digite a base do triângulo: "))
    #Verificação
    if base > 0:
        break
    print("Digite um valor válido (> 0)")

while True:
    altura = float(input("Digite a altura do triângulo: "))
    #Verificação
    if altura > 0:
        break
    print("Digite um valor válido (> 0)")

area = (base * altura) / 2

print("A área do triângulo de base =", base, "e altura =", altura, "é", area)