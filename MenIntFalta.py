lista = []
ordenada = []
tamanho = int(input())
i = 0
while i < tamanho:
    lista.append(int(input()))
    i = i+1

l2 = sorted(lista)
for i in l2:
    if i > 0:
    	ordenada.append(i)
maior = ordenada[len(ordenada)-1]
falta = maior+1
hold = 0
for i in range(0, len(ordenada)):
    menor = ordenada[i]
    if i < len(ordenada)-1 and menor+1 != ordenada[i+1] and hold ==0:
        if menor+1 >= 0:
            falta = menor+1
            hold = 1

print (falta)
