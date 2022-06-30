def verifica_par(x):
    return x % 2 == 0

def calcula_fatorial(x):
    fatorial = x
    for i in range(2,x):
        fatorial *= i
    return fatorial

def encontra_divisores(x):
    divisores = []
    for n in range(1, x+1):
        if x % n == 0:
            divisores.append(n)
    return divisores

def verifica_primo(x):
    return len(encontra_divisores(x)) == 2