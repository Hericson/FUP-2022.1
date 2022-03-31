import os
os.system('cls' if os.name == 'nt' else 'clear')

# Problema 3

# Faça um programa que leia uma quantidade inteira de dinheiro (em R$) e retorne as quantidades mı́nimas de notas nos valores de R\\$100, R$50, R$20, R$10, R$5, R$2 e R$1 (moeda) em que o valor pode ser convertido.

# Dinheiro = R$173

# Nota R$100 = 1

# Nota R$50 = 1

# Nota R$20 = 1

# Nota R$2 = 1

# Moeda R$1 = 1

total_dinheiro = int(input("Digite uma quantidade inteira de dinheiro: R$ "))
print(f"Dinheiro = R$ {total_dinheiro}")

notas_100 = total_dinheiro // 100
resto = total_dinheiro % 100

if notas_100 > 0:
    print(f"Nota R$ 100: {notas_100}")

notas_50 = resto // 50
resto = resto % 50

if notas_50 > 0:
    print(f"Nota R$ 50: {notas_50}")

notas_20 = resto // 20
resto = resto % 20

if notas_20 > 0:
    print(f"Nota R$ 20: {notas_20}")

notas_10 = resto // 10
resto = resto % 10

if notas_10 > 0:
    print(f"Nota R$ 10: {notas_10}")

notas_5 = resto // 5
resto = resto % 5

if notas_5 > 0:
    print(f"Nota R$ 5: {notas_5}")

notas_2 = resto // 2
resto = resto % 2

if notas_2 > 0:
    print(f"Nota R$ 2: {notas_2}")

moedas_1 = resto

if moedas_1 > 0:
    print(f"Moeda R$ 1: {moedas_1}")












  





