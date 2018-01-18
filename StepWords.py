
import operator
StepWords = []
words = []
wordfreq = []
gamb = []
merge = []
sw = open("/home/xayah/Área de Trabalho/blabla", "r")   #aqui é pras KayWords
fop = open("/home/xayah/Área de Trabalho/texto1", "r")  #aqui é o caminho pro texto

for line in sw:
    StepWords.append(line)                  #vetor com StepWords

for line in fop:
    for word in line.split():
        if word not in StepWords:
            words.append(word.lower())      #vetor "limpo" e contendo o texto

#começando a contar a frequencia
for w in words:
    if w not in gamb:
        gamb.append(w)                  #tem as palvras SEM repetições
        wordfreq.append(words.count(w)) #tem as frequencias

#inserindo os vetores no merge "zip"
for i in range(1, len(gamb)):
    merge.append([wordfreq[i], gamb[i]])

#ordenando a matriz pela coluna de frequencias
sortedMerge = sorted(merge, key = operator.itemgetter(0))

print(sortedMerge)
