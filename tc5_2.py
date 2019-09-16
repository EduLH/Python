import numpy as np
from numpy import array
from scipy.linalg import lu
import math

x = np.array([1, 2, 3, 4, 5, 6, 7, 8])
for i in range(0, len(x)):
    x[i] = np.log(x[i])


y = np.array([0.5, 0.6, 0.9, 0.8, 1.2, 1.5, 1.7, 2])
for i in range(0, len(y)):
    y[i] = np.log(y[i])

def normalsum(x):
    soma = 0
    for i in x:
        soma += i
    return(soma)

def sum2(x):
    soma2 = 0
    for i in x:
        soma2 += i*i
    return(soma2)

def sum3(x):
    soma3 = 0
    for i in x:
        soma3 += i*i*i
    return(soma3)

def sum4(x):
    soma4 = 0
    for i in x:
        soma4 += i*i*i*i
    return(soma4)

def indexSum(x, y):
    soma = 0
    for i in zip(x,y):
        soma += i[0] + i[1]
    return(soma)

def indexSum2(x, y):
    soma = 0
    for i in zip(x,y):
        soma += (i[0]*i[0]) + i[1]
    return(soma)

a = array([[len(y), normalsum(x), normalsum(y)],
           [normalsum(x), sum2(x), indexSum(x,y)],
           [0, 0, 0]])
#a = array([[len(y), normalsum(x), sum2(x), normalsum(y)],
#           [normalsum(x), sum2(x), sum3(x), indexSum(x,y)],
#           [sum2(x), sum3(x), sum4(x),indexSum2(x,y)],
#           [0, 0, 0, 0]])

pl, u = lu(a, permute_l=True)
u

XX=[]

for i in range(2, len(u)+1):
    XX.append(u[-i][-1])
    #print((u[-i][-1]))
    for j in range(2, i):
        if j != i:
            XX[-1]=XX[-1]-(u[-i][-j]*XX[-j])
    XX[-1]=XX[-1]/u[-i][-i]

print((len(x)*(math.e**XX[1])) + (normalsum(x)*XX[0]))
#$print((normalsum(x)*XX[2]) + (sum2(x)*XX[1]) + (sum3(x)*XX[0]))
normalsum(y)

def Newton(f, dfdx, x, eps):
    x1 = f(x)
    iteration_counter = 0
    while abs(x1) > eps and iteration_counter < 100:
        x = x - float(x1)/dfdx(x)
        x1 = f(x)
        iteration_counter += 1
    if abs(x1) > eps:
        iteration_counter = -1
    return x, iteration_counter

def f(x):
    return x**2 - 2

def dfdx(x):
    return 2*x

print(Newton(f, dfdx, x=1000, eps=1.0e-6))
