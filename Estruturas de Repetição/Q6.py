# Problema 6

# Faça um programa que leia um número N de termos, calcule e mostre os valores de acordo com a seguinte série: 2, 7, 3, 4, 21, 12, 8, 63, 48, 16, 189, 192, 32, 567, 768...

#Apenas pra limpar o terminal quando executa
import os
os.system('cls' if os.name == 'nt' else 'clear')

cont2 = 0
cont7 = 0
cont3 = 0

for i in range(15):
    if i % 3 == 0:
        print(2 * 2 ** cont2)
        cont2+=1
    elif (i-1) % 3 == 0:
        print(7 * 3 ** cont7)
        cont7+=1
    else:
        print(3 * 4 ** cont3)
        cont3 +=1
        

