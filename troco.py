def troco(quantidade, moedas):
    combinacoes = [0] * (quantidade+1)

    combinacoes[0] = 1

    for moeda in moedas:
        for i in range(1, len(combinacoes)):
            if i >= moeda:
                combinacoes[i] += combinacoes[i - moeda]
                print(combinacoes)
        print("")
    return(combinacoes[quantidade])

print(troco(12, [1, 2, 5]))
