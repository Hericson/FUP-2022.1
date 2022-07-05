def le_receita(nome_arquivo):
    arquivo_receita = open(nome_arquivo, "r")
    linhas = arquivo_receita.readlines()
    arquivo_receita.close()

    receita = []
    
    for linha in linhas:
        nome, tipo, valor = linha.strip().split(",")
        valor = float(valor)

        receita.append({"nome": nome, "tipo": tipo, "valor": valor})
    return receita


def mostra_tipos_remedios(receita):
    tipos_remedios = {}
    for remedio in receita: # remedio = {"nome":Vitamina D,"tipo": comprimido, "valor": 34.69}
        if remedio['tipo'] not in tipos_remedios:
            tipos_remedios[remedio['tipo']] = 1
        else:
            tipos_remedios[remedio['tipo']] += 1

    for tipo, quantidade in tipos_remedios.items():
        print(f"[{tipo.capitalize()}]: {quantidade}")

def calcula_total_receita(receita):
    total_receita = 0
    for remedio in receita:
        total_receita += remedio['valor']
    return round(total_receita,2)

receita = le_receita("/home/leaddell/Doutorado em Ciência da Computação/Disciplinas/FUP-2022.1/Arquivos/remedios.csv")

mostra_tipos_remedios(receita)

print(f"Valor Total da Receita: R$ {calcula_total_receita(receita)}")