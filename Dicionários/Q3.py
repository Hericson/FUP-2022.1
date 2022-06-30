tabela = [{'times':['Brasil','Itália'],   'faltas':[10, 9]},
          {'times':['Brasil','Espanha'],  'faltas':[5, 7]},
          {'times':['Itália', 'Espanha'], 'faltas':[7, 8]}]

times = {}


def atualiza_time(times, time, faltas):
    if time in times:
        times[time] += faltas
    else:
        times[time] = faltas
    return times


# partida = {'times':['Brasil','Itália'],   'faltas':[10, 9]},
for partida in tabela:
    for i in range(len(partida['times'])):
        atualiza_time(times, partida['times'][i], partida['faltas'][i])

total_faltas = sum(times.values())
mais_faltas = max(times.values())
menos_faltas = min(times.values())
times_mais_faltas = []
times_menos_faltas = []

for time, faltas in times.items():
    if faltas == mais_faltas:
        times_mais_faltas.append(time)
    if faltas == menos_faltas:
        times_menos_faltas.append(time)

print(f'Total de faltas no campeonato: {total_faltas}')
print(f"time(s) que mais fez faltas: {', '.join(times_mais_faltas)} ({mais_faltas} faltas)")
print(f"time(s) que menos fez faltas: {', '.join(times_menos_faltas)} ({menos_faltas} faltas)")
