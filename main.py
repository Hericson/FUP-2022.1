# Problema 8

# Escreva um programa que pede os seguintes dados:

# - Valor do salário de um funcionário
# - Aumento em percentagem

# Depois mostre o valor do aumento e o salário com aumento arredondados para duas casas decimais.

salario_original = float(input("Digite o Salário: R$ "))
aumento_percentual = float(input("Digite o aumento percentual: "))

valor_aumento = salario_original * (aumento_percentual / 100)

salario_atualizado = salario_original + valor_aumento

print("O aumento será de R$", valor_aumento)
print("O novo salário será: R$", salario_atualizado)