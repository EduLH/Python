resultado = []  ##Vetor para analise de caso

resultados = [] ##vetor para salvar casos aceitos

def troco(caixa, goal):
    if goal < 0:    #funcao se baseia em remover valores do GOAL
        return      #caso GOAL seja =0, chegou a um resultado aceitavel

    if goal == 0 and sorted(resultado) not in resultados:   #prevenir resultados identicos
        resultados.append(sorted(resultado))

    else:
        for i in caixa:     #enquanto houver moedas
            resultado.append(i) #adicione uma moeda ao v-resultado
            troco(caixa, goal-i)    #remova o valor da moeda do troco desejado
            print (resultado)
            resultado.pop() #limpa Resultado para as proximas verificacoes

goal = int(input()) #troco desejado
tamam = int(input())    #numero de moedas
moedas = [] #variedade de moedas

for _ in range(tamam): #variedade de moedas
    moedas.append(int(input()))

troco(moedas, goal)

print (resultados)
