resultado = []

resultados = []

def troco(caixa, goal):
    if goal < 0:
        return

    if goal == 0 and sorted(resultado) not in resultados:
        resultados.append(sorted(resultado))

    else:
        for i in caixa:
            resultado.append(i)
            troco(caixa, goal-i)
            resultado.pop()

goal = int(input())
tamam = int(input())
moedas = []
for _ in range(tamam):
    moedas.append(int(input()))
troco(moedas, goal)

print (len(resultados))
