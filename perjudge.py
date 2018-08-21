
def perceptron (semente, alfa, max_epocas, entradas, saidas):
    degrau = lambda u: 1 if u >= 0 else 0
    ativacao = degrau
    random.seed(semente)

    entradas = map(lambda e: [1] + e, entradas)
    nDados = len(entradas)
    nDim = len(entradas[0])

    pesos = [random.random() for _ in range(nDim)]
    for epoca in range(max_epocas):
        soma_erros = 0
        for j in range(nDados):
            potencial = sum([pesos[i]*entradas[j][i] for i in range(nDim)])
            saida_calculada = ativacao(potencial)
            erro = saidas[j] - saida_calculada
            soma_erros += abs(erro)
            pesos = [pesos[i] + (alfa*erro*entradas[j][i]) for i in range(nDim)]
