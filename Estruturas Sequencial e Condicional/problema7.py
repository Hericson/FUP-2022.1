# Problema 7

# Faça um programa que receba três números inteiros e mostre o maior número ı́mpar entre eles (suponha que os números sejam diferentes). Se nenhum deles for ı́mpar, mostre uma mensagem constatando esse fato.

numero_1 = int(input("Digite o primeiro número: "))
numero_2 = int(input("Digite o segundo número: "))
numero_3 = int(input("Digite o terceiro número: "))

#Verificar se os números são ímpares
if numero_1 % 2 == 0 and numero_2 % 2 == 0 and numero_3 % 2 == 0:
    print("Nenhum número é impar")
else:
    maior = 1
    if numero_1 %  2 == 1 and numero_1 > maior:
        maior = numero_1
    if numero_2 % 2 == 1 and numero_2 > maior:
        maior = numero_2
    if numero_3 % 2 == 1 and numero_3 > maior:
        maior = numero_3

    print("Maior ímpar digitado:", maior)
    