#  Problema 4

# Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$80,00 ou em galões de 3,6 litros, que custam R$25,00.

# Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:

# • comprar apenas latas de 18 litros;

# • comprar apenas galões de 3,6 litros;

# • misturar latas e galões, de forma que o preço seja o menor. Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.

nome_local = input("Qual o nome do local a ser pintado? ")
area = float(input("Qual a área a ser pintada (em m2)? "))

cobertura_por_litro = 3
volume_lata = 18
preco_lata = 80
volume_galao = 3.6
preco_galao = 25

quantidade_de_litros = 1.1 * (area / cobertura_por_litro)

quantidade_somente_latas = int(math.ceil(quantidade_de_litros / volume_lata))
preco_total_somente_latas = quantidade_somente_latas * preco_lata

quantidade_somente_galoes = int(math.ceil(quantidade_de_litros / volume_galao))
preco_total_somente_galoes = preco_galao * quantidade_somente_galões

quantidade_latas = int(quantidade_de_litros // volume_lata)
litros_restantes = quantidade_de_litros - (quantidade_latas * volume_lata)

quantidade_galoes = math.ceil(litros_restantes / volume_galao)

preco_total = quantidade_latas * preco_lata + quantidade_galoes * preco_galao

print(f"Para pintar o local {nome_local} será necessário:\n"
      f"-> {quantidade_somente_latas} lata(s) ao custo de R${preco_total_somente_latas:.02f}; ou\n"
      f"-> {quantidade_somente_galoes} galão(ões) ao custo de R${preco_total_somente_galoes:.02f}; ou\n"
      f"-> {quantidade_latas} lata(s) e {quantidade_galoes} galão(ões) ao custo de R${preco_total:.02f}.")
