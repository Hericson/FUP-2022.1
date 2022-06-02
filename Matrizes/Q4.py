tabela = [
    ['Brasil', 'Itália', [10,9]],
    ['Brasil', 'Espanha', [5,7]],
    ['Itália', 'Espanha', [7,8]]
]

times = []
for partida in tabela:
    for time in partida[0:2]:
        if time not in times:
            times.append(time)

faltas = [0] * len(times)

for partida in tabela:
    time_1, time_2 = partida[0:2]
    faltas_1, faltas_2 = partida[2]

    for i in range(len(times)):
        if time_1 == times[i]:
            faltas[i] += faltas_1
        elif time_2 == times[i]:
            faltas[i] += faltas_2

total_faltas = sum(faltas)

mais_faltas = max(faltas)

time_mais_faltas = None

for i in range(len(times)):
    if faltas[i] == mais_faltas:
        time_mais_faltas = times[i]
        break

menos_faltas = min(faltas)
time_menos_faltas = None

for i in range(len(times)):
    if faltas[i] == menos_faltas:
        time_menos_faltas = times[i]
        break

print(f"Total de faltas do campeonato: {total_faltas}")
print(f"Time que mais fez faltas: {time_mais_faltas} com {mais_faltas} faltas")
print(f"Time que fez menos faltas: {time_menos_faltas} com {menos_faltas} faltas")