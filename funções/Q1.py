from regex import I


def imprime_linha(N):
    for i in range(1, N+1):
        print(i, end=" ")
    print("")

def imprime_triangulo(N):
    for i in range(1, N+1):
        imprime_linha(i)
N = int(input("Digite a quantidade de linhas: "))

imprime_triangulo(N)

