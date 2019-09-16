import operator
def distancer(dic, at, t, sol, weight, distance):
    # sanity check
    if at == t:
        distance[t] = weight+1
        return
    if at not in dic:
        return "There is no start node called " + str(at) + "."
    if t not in dic:
        return "There is no terminal node called " + str(t) + "."
    if len(dic[at]) == 0:
        return
    for i in dic[at]:
        #print(len(sol))
        if i not in sol or distance[i] > weight or i == t:
            if i == t:
                if distance[i] > weight:
                    distance[i] = weight
                return
            if distance[i] > weight:
                distance[i] = weight
            if i not in sol:
                sol.append(i)
            distancer(dic, i, t, sol, weight+1, distance)

    return

def opEx4(dic, no):
    sol = []
    temp = []
    cont = 0
    for filho in dic[no]:
        for neto in dic[filho]:
            if neto != no:
                for fim in dic[neto]:
                    if fim == no:
                        temp.append(filho)
                        temp.append(neto)
                        if sorted(temp) not in sol:
                            sol.append(sorted(temp))
                            cont = cont + 1
    return(cont/(len(dic)-1))

def opEx2(dic, distance, atual, target):
    sol = [] #solution nodes
    weight = 1
    distancer(dic, atual, target, sol, weight, distance)
    return(distance[target])

def incident (dic):

    for key, value in dic.items():
        print(len(value))
#Check the all incident verts number on this dictionary

def closeness(dic, distance, item):
    close = 0
    for sec_item in dic:
        close += opEx2(dic, distance, item, sec_item)
    return(close/(len(dic)))

def meinho(dic, distance, item):
    meiou = 0
    for sec_item in dic:
        if(opEx2(dic, distance, item, sec_item) <= 1):
            meiou += 1
    return(meiou)


from collections import OrderedDict
dic = OrderedDict()
distance = OrderedDict()
print("informe o 'path' para o arquivo FBB. Exemplo: /home/MyPc/Desktop/FILE")
path = input()
fileInput = open(path, "r")
#Buffering file
#/home/eduardo/Área de Trabalho/frat_clean.txt
for line in fileInput:
    k, v = line.split()
    dic.setdefault(k, [])
    if v not in dic[k]:
        dic.setdefault(k, []).append(v)

    dic.setdefault(v, [])
    if k not in dic[v]:
        dic.setdefault(v, []).append(k)
    distance[v] = float("inf")
    distance[k] = float("inf")

i = 0
while int(i) == 0:
    print("informe qual operação deseja realizar:")
    print("1 - Para calcular o numero de vertices incidentes em todos os nos do grafo")
    print("2 - Para calcular a distancia minima entre dois nos")
    print("3 - Para saber as medidas de centralidade do nó")
    print("4 - Para saber quantos 'triangulos' existem em um no especifico")
    a = input()
    if int(a) == 1:
        incident(dic)
    if int(a) == 2:
        print("informe o no inicial")
        atual = input()
        print("informe o no que deseja calcular a distancia")
        target =input()
        print(opEx2(dic, distance, atual, target))
    if int(a) == 3:
        print("informe o no que deseja calcular Closeness e Betweenness")
        target =input()
        print(closeness(dic, distance, target))
        print(meinho(dic, distance, target))
    if int(a) == 4:
        print("informe o no que deseja fazer analise")
        no = input()
        print(opEx4(dic, no))
    print("deseja fazer mais alguma operação?")
    print("0 - sim; 1 - não")
    i = input()
