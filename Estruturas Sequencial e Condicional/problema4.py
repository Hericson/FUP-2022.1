import os
os.system('cls' if os.name == 'nt' else 'clear')

# Problema 4

# Faça um programa que leia a duração de um evento em segundos e converta para horas, minutos e segundos.

# Exemplo: Duração = 3785 segundos -> 1 hora, 3 minutos e 5 segundos.

duracao_segundos = int(input("Qual a duração do evento em segundos? "))

horas = duracao_segundos // 3600
resto = duracao_segundos % 3600

minutos = resto // 60
segundos = resto % 60

print("Duração = ", duracao_segundos, " segundos ->", horas, "hora(s)", minutos, "minutos(s) e", segundos, " segundos")

  





