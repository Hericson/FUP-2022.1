def cria_vandermonde(x):
    N = len(x)
    matriz = []

    for i in range(N):
        linha = []
        for exp in range(N):
            linha.append(x[i] ** exp)
        matriz.append(linha)
    
    return matriz

def imprime_matriz(matriz, nome_matriz="Genérica"):
    print(nome_matriz)
    for linha in matriz:
        print(linha)

def converte_vetor(vetor):
    for i in range(len(vetor)):
        vetor[i] = float(vetor[i])
    
    return vetor
    
x_old = input("Informe o vetor de x: ").split(",")

x_new = converte_vetor(x_old)

matriz_vondermonde = cria_vandermonde(x_new)

imprime_matriz(matriz_vondermonde, "Matriz de Vondermonde")




