# Problema 3

# Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R\$80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o
# preço total.

area = float(input("Qual a área a ser pintada (em m2)? "))
nome_local = input("Qual o nome do local a ser pintado? ")
cobertura_por_litro = 3
volume_lata = 18
preco_lata = 80

quantidade_litros = area / cobertura_por_litro
quantidade_de_latas = math.ceil(quantidade_litros / volume_lata)

preco_total = preco_lata * quantidade_de_latas

print(f"Para pintar o local {nome_local} "
      f"serão necessárias {quantidade_de_latas} lata(s) "
      f"ao custo de R$ {preco_total}")