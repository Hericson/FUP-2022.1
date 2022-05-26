"""Problema 6

Faça um programa que preencha um vetor com dez números inteiros e um segundo vetor
com cinco números inteiros, calcule e mostre dois vetores resultantes: 
o primeiro vetor resultante será composto pela soma de cada número par do primeiro vetor
somado a todos os números do segundo vetor. O segundo vetor resultante será composto
pela quantidade de divisores que cada número ı́mpar do primeiro
vetor tem no segundo vetor.


Exemplo:

Primeiro vetor: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

Segundo vetor: [1, 2, 3, 4, 5]

Primeiro vetor resultante: [17, 19, 21, 23, 25]

Segundo vetor resultante: [1, 2, 2, 1, 2]

"""

vetor_1 = []
for i in range(5):
    vetor_1.append(int(input(f"Digite o {i+1}º elemento do vetor 1: ")))

vetor_2 = []
for i in range(5):
    vetor_2.append(int(input(f"Digite o {i+1}º elemento do vetor 2: ")))

soma_vetor_2 = sum(vetor_2)

vetor_resultante_1 = []
vetor_resultante_2 = []


for x in vetor_1:
    if x % 2 == 0: #Verificar os números pares do primeiro vetor
        vetor_resultante_1.append(x + soma_vetor_2)
    else: #Números Ímpares
        cont_divisores = 0
        for d in vetor_2:
            if x % d == 0:
                cont_divisores += 1
        vetor_resultante_2.append(cont_divisores)

