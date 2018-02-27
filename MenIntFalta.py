lista = []
tamanho = int(input())


for i in range(0,tamanho):
    lista.append(int(input()))

lista = sorted(lista)
save = lista[-1]+1  #salva o ultimo+1 item, caso nao esteja faltando algo

for i in lista:
    if i-1 not in lista:    #se i-1 nao estiver na lista
        if i-1 > 0:
            save = i-1  #ele eh o menor elemento nao presente
            break

print (save)

#teste do itau
print (sum(int(i) for i in str(2**1000)))
#soma do algarismos de 2^1000
