"""
Problema 7

Faça um programa que receba uma frase e, a cada duas palavras dela, 
realize uma criptografia da seguinte forma: a primeira letra da primeira palavra 
da frase concatenada com a última letra da segunda palavra, concatenada com a 
segunda letra da primeira palavra e com a penúltima letra da segunda palavra 
e assim por diante. No caso de quantidade de palavras ı́mpares, a última palavra 
deve simplesmente ser invertida. 

Exemplo:

Frase: Casa com janelas coloridas

Saı́da: Cmaosca jsaandeilraosloc
"""

frase = "Casa com janelas coloridas lindas"
palavras = frase.split(" ")
frase_criptografada = ""

#Percorre as palavras
for i in range(0, len(palavras)-1, 2):
    tamanho_maximo = max(len(palavras[i]), len(palavras[i+1]))
    #Percorre os caracteres da palavra
    for j in range(tamanho_maximo):
        if j < len(palavras[i]):
            frase_criptografada += palavras[i][j]
        if j < len(palavras[i+1]):
            frase_criptografada += palavras[i+1][-1-j]
    frase_criptografada += " "

if len(palavras) % 2 == 1:
    frase_criptografada += palavras[-1][::-1]

print(f"Frase original: {frase}")
print(f"Frase criptografada: {frase_criptografada}")
