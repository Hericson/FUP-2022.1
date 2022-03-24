# Problema 7

# Faça um programa que receba um número positivo e maior que zero, calcule e mostre:

# a) o número digitado ao quadrado

# b) o número digitado ao cubo

# c) a raiz quadrada do número digitado

# d) a raiz cúbica do número digitado

x = int(input("Digite um número inteiro positivo: "))

print(x, "ao quadrado =", x**2)
print(x, "ao cubo =", x**3)
print("Raiz quadrada de ", x , " = ", x ** (1/2))
print("Raiz cúbica de ", x, " = ", x ** (1/3))