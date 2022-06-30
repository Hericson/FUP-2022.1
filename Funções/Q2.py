def converte_24_12(horario_24):
    """
    Função que recebe um horário no formato 24h e retorna no formato 12h
    Args:
        horario_24 (str): Horário no formato 24H (HH:MM)

    Returns:
        str: Horário no formato 12H concatenado com o turno
    """
    idx_dois_pontos = horario_24.find(":")
    hora = int(horario_24[:idx_dois_pontos])
    turno = 'A.M.'

    if hora > 12:
        hora = hora - 12
        turno = 'P.M.'
    
    return str(hora) + horario_24[idx_dois_pontos:] + " " + turno
    

while True:
    horario_24 = input("Qual a hora atual no formato 24h (HH:MM)? ")

    print(f"São {converte_24_12(horario_24)}")

    if input("Deseja continuar (s/n)? ").lower() != 's':
        break