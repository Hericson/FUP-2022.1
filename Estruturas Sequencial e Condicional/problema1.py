import os
os.system('cls' if os.name == 'nt' else 'clear')

# Problema 1

# Leia três valores para os lados de um triângulo, considerando lados como: A, B e C. Verifique se os lados fornecidos formam realmente um triângulo. Isso pode ser feito se certificando que A < B + C para qualquer permutação dos lados.

# Se esta condição for verdadeira, deve ser indicado qual tipo de triângulo foi formado: isósceles, escaleno ou equilátero.

#Lê os dados
lado_A = float(input("Digite o valor de A: "))
lado_B = float(input("Digite o valor de B: "))
lado_C = float(input("Digite o valor de C: "))

#Testar se o triângulo existe

if lado_A < lado_B + lado_C and lado_B < lado_A + lado_C and lado_C < lado_A + lado_B:
    print("O triângulo existe!")

    #Verificar o tipo de triângulo
    if lado_A == lado_B == lado_C:
        print("O triângulo é equilátero!")
    elif lado_A != lado_B and lado_B != lado_C and lado_A != lado_C:
        print("O triângulo é escaleno!")
    else:
        print("o triângulo é isósceles!")
else:
    print("O triângulo não existe!")

    
    





