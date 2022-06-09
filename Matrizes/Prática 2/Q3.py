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

    flag_simetrica = True
    for i in range(N):
        for j in range(N):
            if matriz[i][j] != matriz[j][i]:
                flag_simetrica = False
                break
        
        if flag_simetrica == False:
            break

    if flag_simetrica:
        print("A matriz é simétrica")
    else:
        print("A matriz não é simétrica")
