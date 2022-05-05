# Problema 8

# Uma companhia de teatro deseja montar uma série de espetáculos. A direção calcula que, a R$5,00 o ingresso, serão vendidos 120 ingressos, e que as despesas serão de R$200,00. Diminuindo-se em R$0,50 o preço dos ingressos, espera-se que as vendas aumentem em 26 ingressos. Faça um programa que escreva uma tabela de valores de lucros esperados em função do preço do ingresso, fazendo-se variar esse preço de R$5,00 a R$1,00, de R$0,50 em R$0,50. Ao final, escreva o preço em que o lucro máximo é obtido.

#Apenas pra limpar o terminal quando executa
import os
os.system('cls' if os.name == 'nt' else 'clear')

despesa = 200
preco = 5
ingresso = 120
melhor_lucro = -1
melhor_preco = 0

print("Preço\t\tIngressos\tLucro")

while preco >= 1:

    ingressos = 120 + 26 * (5-preco) * 2
    lucro = (ingressos * preco) - despesa
    print(f"R${preco:.2f} \t\t {ingressos:.0f} \t\t R${lucro:.2f}")

    if lucro > melhor_lucro:
        melhor_lucro = lucro
        melhor_preco = preco

    # preco = preco - 0.5
    preco -= 0.5

print(f"Com o preço de R${melhor_preco:.2f} serão vendidos {ingressos:.0f} ingressos e o lucro será R${melhor_lucro:.2f}")


    






