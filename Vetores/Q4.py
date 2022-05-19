import os
os.system('cls' if os.name == 'nt' else 'clear')

# Problema 4

# Um palíndromo é uma sequência de caracteres cuja leitura é idêntica se feita da direita para esquerda ou vice−versa. Por exemplo: OSSO e OVO são palíndromos. Em textos mais complexos os espaços e pontuação são ignorados. A frase SUBI NO ONIBUS é o exemplo de uma frase palíndroma onde os espaços foram ignorados. Faça um programa que leia uma sequência de caracteres, mostre−a e diga se é um palíndromo ou não.

frase = input("Digite uma frase: ")

caracteres = frase.upper().replace(" ", "")

for i in range(len(caracteres) // 2):
    if caracteres[i] != caracteres[-1-i]:
        print("Não é um palíndromo")
        break
else:
    print("É um palíndromo")

