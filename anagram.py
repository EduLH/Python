import collections

palavra1 = input() #palavra1
palavra2 = input() #palavra2
a = 0
c = collections.Counter(palavra1)  #Mapeia a P1
d = collections.Counter(palavra2)  #Mapeia a P2
for i in c:
    if d[i] !=0:
        if c[i] <= d[i]:
             a = a + c[i]
        else:
             a = a + d[i]

print(a)
