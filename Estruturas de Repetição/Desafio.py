# Faça um programa que receba um valor A e verifique o maior primo menor que A

a = int(input("Digite um número inteiro positivo A: "))
primo = None
cont = 0
##Testar de 2 até A
for x in range(2, a):
    ##Saber se x é primo
    for i in range(2, x):
        if x % i == 0:
            # print(x, "não é primo")
            break
    else:
        primo = x
        # break
        # print("é primo")
    cont += 1

print(f"O maior primo menor que {a} é {primo}")
print(f"Foram necessárias {cont} iterações")


