from regex import I


matriz_A = []
matriz_B = []
matriz_C = []

ordem = 3

for i in range(ordem):
    linha = [0] * ordem
    matriz_A.append(linha.copy())
    matriz_B.append(linha.copy())
    matriz_C.append(linha.copy())

lista_numeros = [1,2,5,7,8,9,6,2,4]

cont = 0
for i in range(ordem):
    for j in range(ordem):
        matriz_A[i][j] = lista_numeros[cont]
        matriz_B[j][i] = lista_numeros[cont]
        cont += 1

for i in range(ordem):
    for j in range(ordem):
        matriz_C[i][j] = matriz_A[i][j] * matriz_B[i][j]

print("Matriz A digitada:")
for linha in matriz_A:
    print(linha)

print("Matriz B digitada:")
for linha in matriz_B:
    print(linha)

print("Matriz C calculada:")
for linha in matriz_C:
    print(linha)


    


