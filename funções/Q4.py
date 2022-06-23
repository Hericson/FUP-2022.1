import lib

x = int(input("Digite um número inteiro positivo: "))

print(f"{x} é um número {'par' if lib.verifica_par(x) else 'ímpar'}.")
print(f"O fatorial de {x} é {lib.calcula_fatorial(x)}.")
print(f"Os divisores de {x} são {lib.encontra_divisores(x)}.")
print(f"{x}{'' if lib.verifica_primo(x) else ' não'} é primo")