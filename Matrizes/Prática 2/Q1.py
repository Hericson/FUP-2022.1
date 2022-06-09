N = int(input("Informe a ordem da matriz: "))

matriz = []
for i in range(N):
    linha = []
    for j in range(N):
        linha.append(float(input(f"Digite o elemento [{i}][{j}]: ")))
    matriz.append(linha)


print("Matriz Digitada: ")
for linha in matriz:
        print(linha)

#Diagonal Principal
diagonal_principal = []
for i in range(N):
        diagonal_principal.append(matriz[i][i])

print(f"Diagonal Principal: {diagonal_principal}")

#Diagonal Secundária
diagonal_secundaria = []
for i in range(N):
        for j in range(N):
                if i+j == N-1:
                        diagonal_secundaria.append(matriz[i][j])
print(f"Diagonal Secundária: {diagonal_secundaria}")

nova_matriz = []
for i in range(N):
        linha = matriz[i].copy()
        for j in range(N):
                linha[j] = linha[j] * diagonal_principal[i] + diagonal_secundaria[i]
        nova_matriz.append(linha)
        
print("Nova Matriz: ")
for linha in nova_matriz:
        print(linha)

