import collections
import random
import sys

def avalia_senha(s1, s2):
    x= 0
    for a, b in zip(s1, s2):
        if a == b:
            x += 1
    return x

def cria_ind (tamam_F, opcoes): #GERA INDIVIDUO
    # random.sample retorna uma lista. Logo, pegue o 1o. elemento.
    return [random.sample(opcoes, 1)[0] for i in range(tamam_F)] #retorna UMA lista do tamanho 'tamam_F' letras aleatorias de A-Z
# cria_ind (3, ['a', 'x', 9])   exemplo de INPUT


def cria_pop (tamam_F, tamPop, opcoes): #gera populacao
    return [cria_ind (tamam_F, opcoes) for qtd in range(tamPop)] #retorna uma LISTA de INDIVIDUOS criados
# pop = cria_pop (3, 10, ['a', 'x', 9]) exemplo DE INPUT

def cruzamento (ind1, ind2):#duas strings com possiveis frases
    novo_ind = list(ind1)
    #print(ind1)
    #print(ind2)
    if (len(ind1) < 2 or len(ind1) != len(ind2)): return novo_ind
    else: corte = random.sample(range(1, len(ind1)), 1)[0] # random.sample retorna uma lista. Logo, pegue o 1o. elemento.
    #corta no index do "CORTE" e une as duas strings
    for i in range(corte, len(novo_ind)):
        novo_ind[i] = ind2[i]
    return novo_ind
# cruzamento ([1,1,1], [2,2,2])


def mutacao (ind, probMut, opcoes):
    for i in range(len(ind)):
        if (random.uniform(0, 1) < probMut): #chance de ocorrer mutacao
            ind[i] = random.sample(opcoes, 1)[0]    #mutacao
    return ind
# mutacao(INDIVIDUO, 0.5, [9, 8, 7, 6, 5])



def torneio (aptidao, tamanho):
    id_compet = list(range(len(aptidao))) #ID = tamanho da lista de COMPATIBILIDADE
    competidores = random.sample(id_compet, tamanho)    #Perga ID de 3 competidores
    fit = [aptidao[idx] for idx in competidores]    #cria um VET de aptidao
    v1 = competidores[fit.index(min(fit))]          #Pega o INDEX c menor item

    id_compet.remove(v1)
    competidores = random.sample(id_compet, tamanho)    #Perga ID de 3 competidores
    fit = [aptidao[idx] for idx in competidores]    #Perga ID de 3 competidores
    v2 = competidores[fit.index(min(fit))]          #Pega o INDEX com menor item

    return v1, v2
#input: VETOR DE COMPATIBILIDADE COM A SENHA , INPUT(3 > tamanho do torneio)

def ga(fun, senha, tamam_F, opcoes, tamPop, tamTorneio, probMut, porcCr, nGeracoes):
    pop = cria_pop (tamam_F, tamPop, opcoes)       #inicia uma populacao ~uma LISTA~
    aptidao = [fun(indiv, senha) for indiv in pop] #vetor de avaliacao INDIVIDUO - SENHA
    #REMINDER: TODOS os INDIVIDUOS sao compostos de ums STRING aleatoria do MESMO tamanho
    #da string original. 2o INPUT

    for geracao in range(nGeracoes): #rodando geracoes
        for cruzamentos in range( int(tamPop*porcCr) ): #procriacoes
            vencedor1, vencedor2 = torneio(aptidao, tamTorneio) #pega os caras c "menor" aptidao

            pai1 = pop[vencedor1]
            pai2 = pop[vencedor2]
            filho = cruzamento (pai1, pai2) #pedacos de cada PAI
            filho = mutacao (filho, probMut, opcoes)#mutar o filho

            # Inserir na pop para depois selecionar apenas os melhores
            pop.append(filho)
            aptidao.append(fun(filho, senha))

        # Somente os melhores sobrevivem. Pra isso, descubra a ordem decrescente
        # da aptidao, da melhor para a pior
        # Ordenar a lista [0, ..., tamPop-1] usando os valores de aptidao como referencia
        ordem = sorted(range(len(aptidao)), key=lambda k: aptidao[k], reverse=True)

        # Selecionar os tamPop melhores
        for idx in range(tamPop):
            aptidao[idx] = aptidao[ ordem[idx] ]
            pop[idx] = pop[ ordem[idx] ]

        # Eliminar o restante
        aptidao = aptidao[:tamPop]
        pop = pop[:tamPop]

        if False:
            print ("Ger:", ger, "  fit=", aptidao[0], " Melhor sol=", ''.join(pop[0]),
            "  pior sol=", ''.join(pop[tamPop-1]))

        # Criterio de parada: a quantidade de acertos == tamanho da senha
        if (aptidao[0] == tamam_F):
            break

    return ''.join(pop[0])


########################
# Main
########################

# Le a linha com as configuracoes
config = sys.stdin.readline().strip().split(';')

random.seed(int(config[0]))

opcoes = "abcdefghijklmnopqrstuvwxyz "

# Chama a funcao sa com os parametros lidos
result = ga(fun=avalia_senha,       #bind da funcao FUN com avalia_senha
            senha=config[1],        #frase
            tamam_F=len(config[1]),    #tamanho da frase
            opcoes=opcoes,          #a-z
            tamPop=int(config[2]),  #100
            tamTorneio=int(config[3]),  #3
            probMut=float(config[4]),   #0.1 probabilidade de mutar
            porcCr=float(config[5]),    #0.1 porcentagem de CR?
            nGeracoes=int(config[6]))   #1000

print (result)
