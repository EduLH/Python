import sys

def bpl(grafo, inicio, fim):
    fila = []
    fila.append([inicio])
    while fila:
        caminho = fila.pop(0)
        no = caminho[-1]
        if no == fim:
            return caminho
        for adjacente in grafo.get(no, []):   # Caso nao haja o no, retorne []
            if adjacente not in caminho:  # Caso ainda nao tenha sido visitado
               novo_caminho = list(caminho)
               novo_caminho.append(adjacente)
               fila.append(novo_caminho)
               if adjacente == fim:
                   return (novo_caminho)
    return []

grafo = {}
dados = sys.stdin.readline().strip().split(' ')
inicio, fim = dados[0], dados[1]
for dados in sys.stdin:
    dados = dados.strip().split(' ')
    if dados:
        grafo [dados[0]] = dados[1:]
    else:
        break
print (bpl(grafo, inicio, fim))
