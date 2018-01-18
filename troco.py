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
#
goal = int(input())
tamam = int(input())
Zeca = []
for _ in range(tamam):
    Zeca.append(int(input()))
troco(Zeca, goal)

print (len(resultados))
