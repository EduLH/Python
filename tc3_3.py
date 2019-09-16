from numpy import array
from scipy.linalg import lu

a = array([[1.,1.,1.,400.],
          [1.,1.,2.,600.],
          [2.,3.,5.,1500.],
          [0.,0.,0.,0.,]])


pl, u = lu(a, permute_l=True)

x=[]

for i in range(2, len(u)+1):
    x.append(u[-i][-1])
    print((u[-i][-1]))
    for j in range(2, i):
        if j != i:
            x[-1]=x[-1]-(u[-i][-j]*x[-j])
    x[-1]=x[-1]/u[-i][-i]
