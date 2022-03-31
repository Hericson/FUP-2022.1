import os
os.system('cls' if os.name == 'nt' else 'clear')

# Problema 6

# Faça um programa que receba a medida de um ângulo em graus. Calcule e mostre o quadrante em que se localiza esse ângulo. Considere os quadrantes da trigonometria e, para ângulos maiores que 360◦ ou menores que -360◦ reduzi-los, mostrando também o número de voltas e o sentido da volta (horário ou anti-horário).

  
angulo = float(input("Digite um ângulo (Em graus): "))
angulo_reduzido = abs(angulo) % 360
voltas = abs(angulo) // 360

if angulo < 0:
    sentido = "horário"
else:
    sentido = "anti-horário"

if angulo_reduzido > 0 and angulo_reduzido <= 90:
    quadrante = 1
elif angulo_reduzido > 90 and angulo_reduzido <=180:
    quadrante = 2
elif angulo_reduzido > 180 and angulo_reduzido <= 270:
    quadrante = 3
else:
    quadrante = 4

print("O ângulo", angulo, "graus pode ser reduzido a", angulo_reduzido, "graus, está no quadrante", quadrante, "correspondendo a ", voltas, "voltas no sentido", sentido)
    







