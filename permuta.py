#Trabalho para a dissiplina de AED-II d na UNIFESP
#Marcos Eduardo Lopes Honorato. RA: 86379
#Nota: Este algoritimo de Permutação funciona, no entanto
#estou tendo problemas para passar uma STRING como parametro em função

cont = input()
palavras = []
for i in range (1,cont):
    neo = input()
    palavras.append(''.join(sorted(neo)))

for i in palavras:
    j = 0
    Permusiva(palavras[j], 0)
    j = j+1

def Permusiva(palavras[a], k): #suposto "bug"
    if k == len(palavras[a]):
        print palavras[a]
    else:
        j = len(palavras[a]) -1
        for i in range (0, j):
             trocaCarac(palavras[a], k, i)
             Permusiva(palavras[a], k+1)
             trocaCarac(palavras[a], i, k)

def trocaCarac(palavras[index], p1, p2):
    a = palavras[index]
    a[p1] = a[p2]
