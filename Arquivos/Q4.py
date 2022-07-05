arquivo_usuarios = open("/home/leaddell/Doutorado em Ciência da Computação/Disciplinas/FUP-2022.1/Arquivos/usuarios.txt", 'r')

usuarios = {}
for linha in arquivo_usuarios.readlines():
    nome, tamanho = linha.strip().split(" ")
    usuarios[nome.strip()] = int(tamanho)
arquivo_usuarios.close()

tamanho_total = sum(usuarios.values())

arquivo_relatorio = open("/home/leaddell/Doutorado em Ciência da Computação/Disciplinas/FUP-2022.1/Arquivos/relatorio.txt", 'w')

cabecalho = f"ACME Inc.               Uso do espaço em disco pelos usuários\n" \
            f"------------------------------------------------------------------------\n" \
            f"Nr.\tUsuário\t\tEspaço utilizado\t% do uso\n"

print(cabecalho, end="")
arquivo_relatorio.write(cabecalho)

cont = 0
for usuario, tamanho in usuarios.items():
    cont += 1
    linha = f"{cont}\t{usuario:<15}\t{tamanho/2**20:<8.2f} MB\t\t{100*tamanho/tamanho_total:<5.2f} %\n"
    print(linha, end="")
    arquivo_relatorio.write(linha)
    
arquivo_relatorio.close()
