# Problema 6

# Escreva as tabuadas de multiplicar dos números naturais entre 1 e 10.

import os
os.system('cls' if os.name == 'nt' else 'clear')

for i in range(1,11):
    print(f"Tabuada do número {i} ")
    for j in range(1,11):
        t = i * j
        print(f"{i} x {j} = {t}")
    