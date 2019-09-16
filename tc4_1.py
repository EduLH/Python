from numpy import array
import numpy as np
from scipy.linalg import lu

a = array([[5.,1.,1.,5.],
          [3.,4.,1.,6.],
          [3.,3.,6.,0.]])

jacob = []
results = []
new_res = []
for x in range(0, len(a)):
    div = 1/a[x][x]
    jacob.append(np.delete(a[x], x))
    for num in range(0, len(jacob[x])):
        if jacob[x][num] == jacob[x][-1]:
            jacob[x][num] = (jacob[x][num] * (div))
        else:
            jacob[x][num] = (jacob[x][num] * (div) * (-1))
    results.append(0)

for i in range(0, 13): #sla mano, tem q ver isso ae
    for iterator in range(0, len(results)):
        index = 0
        novo_item = 0
        for x in range(0, len(jacob[iterator])-1):
            if(iterator == x):
                index = index+1
            novo_item = novo_item + results[index]*jacob[iterator][x]
        novo_item = novo_item + jacob[iterator][-1]
        new_res.append(novo_item)
    print("results")
    print(results)
    del results[:]
    results = new_res.copy()
    del new_res[:]
