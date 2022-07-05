arquivo_alunos = open('/home/leaddell/Doutorado em Ciência da Computação/Disciplinas/FUP-2022.1/Arquivos/alunos.txt', 'r')
arquivo_notas = open('/home/leaddell/Doutorado em Ciência da Computação/Disciplinas/FUP-2022.1/Arquivos/notas.txt', 'r')

def cria_avaliacao(notas):
    return {"AP1": notas[0], "AP2": notas[1], "AP3": notas[2], "media": round(sum(notas) / len(notas),2)}

diario = {}

for aluno in arquivo_alunos:
    notas = [ float(nota) for nota in arquivo_notas.readline().strip().split("\t")]
    
    diario[aluno.strip().capitalize()] = cria_avaliacao(notas)

arquivo_alunos.close()
arquivo_notas.close()

def mostra_avaliacao(diario, aluno):
    if aluno in diario:
        print(f"Notas de {aluno}:")
        print(f"AP1:\t{diario[aluno]['AP1']:.1f}")
        print(f"AP2:\t{diario[aluno]['AP2']:.1f}")
        print(f"AP3:\t{diario[aluno]['AP3']:.1f}")
        print(f"Média:\t{diario[aluno]['media']:.1f}")
    else:
        print("Aluno Não encontrado")

nome = input("digite o nome de um aluno: ")

mostra_avaliacao(diario, nome)

