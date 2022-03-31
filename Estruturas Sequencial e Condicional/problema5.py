import os
os.system('cls' if os.name == 'nt' else 'clear')

# Problema 5

# Faça um programa que determine a data cronologicamente maior entre duas datas fornecidas pelo usuário. Cada data deve ser composta por três valores inteiros, em que o primeiro representa o dia, o segundo, o mês e o terceiro, o ano.

dia1 = int(input("Digite o dia da data1: "))
mes1 = int(input("Digite o mês da data1: "))
ano1 = int(input("Digite o ano da data1: "))

dia2 = int(input("Digite o dia da data2: "))
mes2 = int(input("Digite o mês da data2: "))
ano2 = int(input("Digite o ano da data2: "))

if ano1 != ano2:
    if ano1 > ano2:
        print("A data 1 é maior")
    else:
        print("A data 2 é maior")
else:
    if mes1 != mes2:
        if mes1 > mes2:
            print("A data 1 é maior")
        else:
            print("A data 2 é maior")
    else:
        if dia1 != dia2:
            if dia1 > dia2:
                print("A data 1 é maior")
            else:
                print("A data 2 é maior")
        else:
            print("As datas são iguais")
            
            





