import collections

palavra1 = input() #palavra1
palavra2 = input() #palavra2

c = collections.Counter(palavra1)#Mapeia a P1
d = collections.Counter(palavra2)#Mapeia a P2

if c == d:
    print ('true')
else:
    print('false')
