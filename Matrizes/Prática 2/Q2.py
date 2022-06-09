N = int(input("Informe a ordem dos vetores: "))

vetor_a = []
for i in range(N):
    vetor_a.append(float(input(f"Digite o {i+1} o elemento do vetor a: ")))

vetor_b = []
for i in range(N):
    vetor_b.append(float(input(f"Digite o {i+1} o elemento do vetor b: ")))

produto_interno = 0
for i in range(N):
    produto_interno += vetor_a[i] * vetor_b[i]

produto_externo = []

for i in range(N):
    produto_externo.append([0]* N)
    for j in range(N):
        produto_externo[i][j] = vetor_a[i] * vetor_b[j]

print(f"Produto Interno: {produto_interno}")

print("Produto externo")
for linha in produto_externo:
    print(linha)


