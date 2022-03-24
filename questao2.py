# Problema 2

# Faça um programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato. Seu programa deve seguir o modelo de saı́da abaixo:

# + Salário Bruto: R\$

# - IR (11%): R\$

# - INSS (8%): R\$

# - Sindicato (5%): R$

# = Salário Liquido: R$

valor_hora = float(input("Quanto você ganha por hora? R$"))

horas_trabalhadas = float(input("Quantas horas você trabalha no mês?"))

salario_bruto = valor_hora * horas_trabalhadas

imposto_renda = salario_bruto * 0.11

inss = salario_bruto * 0.08

sindicato = salario_bruto * 0.05

salario_liquido = salario_bruto - imposto_renda - inss - sindicato

print("+ Salário Bruto: R$", salario_bruto)
print("- IR: R$", imposto_renda)
print("- INSS: R$", inss)
print("- Sindicato: R%", sindicato)
print("= Salário Líquido: R$", salario_liquido)