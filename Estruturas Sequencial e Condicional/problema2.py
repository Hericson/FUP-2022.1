import os
os.system('cls' if os.name == 'nt' else 'clear')

# Problema 2

# Leia três valores para os lados de um triângulo, considerando lados como: A, B e C. Verificar se os lados fornecidos formam realmente um triângulo. Se esta condição for verdadeira, deve ser indicado qual tipo de triângulo foi formado: retângulo, obtusângulo ou acutângulo.

# Dica: Considerando A o maior lado:
# + A^2 = B^2 + C^2 → triângulo retângulo.
# + A^2 > B^2 + C^2 → triângulo obtusângulo.
# + A^2 < B^2 + C^2 → triângulo acutângulo.

#Lê os dados
lado_A = float(input("Digite o valor de A: "))
lado_B = float(input("Digite o valor de B: "))
lado_C = float(input("Digite o valor de C: "))

#Testar se o triângulo existe

if lado_A < lado_B + lado_C and lado_B < lado_A + lado_C and lado_C < lado_A + lado_B:
    print("O triângulo existe!")

    if lado_A ** 2 == lado_B ** 2 + lado_C ** 2:
        print("O triângulo é retângulo!")
    elif lado_A ** 2 > lado_B ** 2 + lado_C ** 2:
        print("o triângulo é obtusângulo")
    else:
        print("O triângulo é acutângulo")

else:
    print("O triângulo não existe!")




  





