import os
os.system('cls' if os.name == 'nt' else 'clear')

# Problema 3

# Escreva um programa que leia uma string e mostre quantas vezes cada caractere aparece nessa string. Não diferencie maiúsculas e minúsculas.

# Exemplo:

# Digite uma string: TtAaCCc

# T: 2x

# A: 2x

# C: 3x

texto = input("Digite uma string: ").upper()

caracteres = ""
for c in texto:
    if c not in caracteres:
        caracteres += c
        print(f"{c}: {texto.count(c)}x")

