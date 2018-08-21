import math
import random
import sys

def knn(novo_exemplo, entradas, respostas, k):
    melhores =  sorted(
                        [
                         [
                             math.sqrt(
                                 sum(
                                  [(n - e)**2 for n, e in zip(novo_exemplo, entradas[j])]   # Calculo da distancia euclidiana entre dois vetores
                                 )
                             ), respostas[j], "id="+str(j)
                         ] for j in range(len(entradas))
                        ],
                        key=lambda tupla: tupla[0]
                )[:k]

                valores = [m[1] for m in melhores]
    return max(set(valores), key = lambda e: valores.count(e))

config = sys.stdin.readline().strip().split(';')

random.seed(int(config[0]))

nDim = int(config[1])
tamTreino = int(config[2])
tamTeste = int(config[3])

cores = ['r', 'b', 'g', 'k', 'm']

dadosTreino = [ [random.uniform(-1.0, 1.0) for i in range(nDim)]  for j in range(tamTreino)]
dadosTeste = [ [random.uniform(-1.5, 1.5) for i in range(nDim)]  for j in range(tamTeste)]

respTreino = [random.choice(cores[:nDim]) for _ in range(tamTreino)]
respTeste =  [random.choice(cores[:nDim]) for _ in range(tamTeste)]

vetK = [1, 3, 5]
for valK in vetK:
    erros = []
    estimado = []

    for i in range(tamTeste):
        estimado.append(knn(dadosTeste[i], dadosTreino, respTreino, valK))
    correct = 0
    for x in range(tamTeste):
        if respTeste[x] == estimado[x]:
            correct+=1
    acuracia = float(correct)/tamTeste
    print ("%.3f" % acuracia)
