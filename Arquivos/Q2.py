arquivo = open('/home/leaddell/Doutorado em Ciência da Computação/Disciplinas/FUP-2022.1/Arquivos/boletim.txt', 'r')

diario = {}

arquivo.readline()

for linha in arquivo.readlines(): #mary	9.0	8.5
    nome, nota1, nota2 = linha.strip().split("\t")
    diario[nome.strip().capitalize()] = [float(nota1.strip()), float(nota2.strip())]

arquivo.close()

arquivo2 = open('/home/leaddell/Doutorado em Ciência da Computação/Disciplinas/FUP-2022.1/Arquivos/boletim_final.txt', 'w')

for nome, notas in diario.items():
    media = sum(notas) / len(notas)

    situacao = "Aprovado" if media >=7 else "Reprovado"

    print(f"{nome}:\tNota1 = {notas[0]:.1f}\tNota2 = {notas[1]:.1f}\tMédia = {media:.1f}\tSituação = {situacao}")

    arquivo2.write(f"{nome}:\tNota1 = {notas[0]:.1f}\tNota2 = {notas[1]:.1f}\tMédia = {media:.1f}\tSituação = {situacao}\n")

arquivo2.close()