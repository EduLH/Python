lista = []
tamanho = int(input())


for i in range(0,tamanho):
    lista.append(int(input()))

save = lista[-1]

lista = sorted(lista)
for index, valor in enumerate(lista) :

    if valor+1 != lista[index+1]:
        if valor+1 > 0:
            save = valor+1
            break

print (save)

#teste do itau
print (sum(int(i) for i in str(2**1000)))
#soma do algarismos de 2^1000
