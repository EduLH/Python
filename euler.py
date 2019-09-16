import math
def euler(f,y0,temp,iter,h):
  t,y = temp,y0
  while t <= iter:
    print ("%6.3f %6.3f" % (t,y))
    t += h
    y += h * fx(t,y)

euler(fx,100,0,10000,5) #Altere estes parametros
#y0, tempoInicial, NumMax para iteracoes, H

def fx(time, X):
    a = 0.1*(math.sqrt(X))*1000 - X
    if(1000-X < 0):
        b = math.sqrt((1000-X)*(-1))
    else:
        b = math.sqrt(1000-X)
    return (a/b)

def rKN(x, fx, n, hs):
    k1 = []
    k2 = []
    k3 = []
    k4 = []
    xk = []
    for i in range(n):
        k1.append(fx[i](x)*hs)
    for i in range(n):
        xk.append(x[i] + k1[i]*0.5)
    for i in range(n):
        k2.append(fx[i](xk)*hs)
    for i in range(n):
        xk[i] = x[i] + k2[i]*0.5
    for i in range(n):
        k3.append(fx[i](xk)*hs)
    for i in range(n):
        xk[i] = x[i] + k3[i]
    for i in range(n):
        k4.append(fx[i](xk)*hs)
    for i in range(n):
        x[i] = x[i] + (k1[i] + 2*(k2[i] + k3[i]) + k4[i])/6
    return x
