import os
os.system('cls' if os.name == 'nt' else 'clear')

# Problema 2

# Uma pessoa gostaria de fazer uma viagem que custa uma quantia V em reais e precisa de ajuda com o planejamento. A pessoa está disposta a fazer uma poupança iniciando em I reais e irá depositar mensalmente uma quantia M na poupança. Sabendo que a poupança rende 0,5% ao mês, faça um programa que receba esses dados do usuário e estime em quantos meses ele conseguiria o dinheiro para viajar.

custo_viagem = float(input("Qual o custo da viagem? R$"))
poupanca_inicial = float(input("Qual o valor inicial da poupança? R$"))
deposito_mensal = float(input("Qual o depósito mensal? R$"))

rendimento_poupanca = 0.5 / 100

total = poupanca_inicial
tempo = 0

while total <= custo_viagem:
    total += deposito_mensal
    total += rendimento_poupanca * total
    tempo += 1

print("Em", tempo, "meses você terá reunido R$", round(total, 2))

