M = int(input("Qual a ordem da matriz quadrada? "))

matriz = []
maior_elemento = None
linha_maior_elemento = None

for i in range(M):
    linha = []
    for j in range(M):
        linha.append(int(input(f"Digite o elemento [{i}][{j}]: ")))
        if maior_elemento is None or linha[-1] > maior_elemento:
            maior_elemento = linha[-1]
            linha_maior_elemento = i
    matriz.append(linha)

minimax = min(matriz[linha_maior_elemento])

print("Matriz digitada: ")
for linha in matriz:
    print(linha)

print(f"Valor Minimax: {minimax} está na linha {linha_maior_elemento+1}")


    