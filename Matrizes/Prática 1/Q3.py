matriz_A = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12]  
]

matriz_B = [
    [13,14,15,16],
    [17,18,19,20],
    [21,22,23,24]
]

matriz_C = []

for i in range(3):
    matriz_C.append(matriz_A[i] + matriz_B[i])

matriz_C_transposta = []

for j in range(len(matriz_C[0])):
    linha = []
    for i in range(len(matriz_C)):
        linha.append(matriz_C[i][j])
    matriz_C_transposta.append(linha)

print("Matriz A digitada:")
for linha in matriz_A:
    print(linha)

print("Matriz B digitada:")
for linha in matriz_B:
    print(linha)

print("Matriz C calculada:")
for linha in matriz_C:
    print(linha)

print("Matriz C transposta:")
for linha in matriz_C_transposta:
    print(linha)