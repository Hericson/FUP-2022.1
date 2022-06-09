while True:
    N = int(input("Informe a ordem da matriz: "))
    if N <= 1:
        break

    matriz = []

    for i in range(N):
        linha = []
        for j in range(N):
            linha.append(float(input(f"Digite o elemento [{i}][{j}]: ")))
        matriz.append(linha)

    print("Matriz Digitada")
    for linha in matriz:
        print(linha)

    diagonal_principal = []

    #diagonal principal
    for i in range(N):
        diagonal_principal.append(matriz[i][i])

    flag_dominante = True
    for i in range(N):
        soma_linha = 0
        for j in range(N):
            if i!=j:
                soma_linha += abs(matriz[i][j])

        if abs(diagonal_principal[i]) <= soma_linha:
            flag_dominante = False
            break

    if flag_dominante:
        print('Estritamente Dominante')
    else:
        print('Não é estritamente dominante')

