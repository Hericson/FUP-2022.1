"""
Problema 8

Faça um programa que leia uma frase do usuário e exibe cada palavra com seus 
caracteres invertidos. Não utilize funções de ordenamento/revertimento
já existentes neste programa.

Exemplo:

"Adoro trabalhar com strings" -> "orodA rahlabart moc sgnirts"
"""

frase = input("Digite uma frase: ")

palavras = frase.split(" ")
nova_frase = ""

for palavra in palavras:
    for idx_letra in range(len(palavra)):
        nova_frase += palavra[-1-idx_letra]
    nova_frase += " "

print(f"{frase} -> {nova_frase}")



