import sys
import random
import math
def objfun(x):
  return 10 * math.sin(0.3 * x) * math.sin (1.3 * x**2) + 0.00001 * x**4 + 0.2*x + 80

def Vizinho (S, li, ls, passo):
    Si = S + random.uniform(-passo, passo)
    if (Si < li):
        Si = li
    elif (Si > ls):
        Si = ls
    return Si

def sa (fun, S0, li, ls, maxIter, alfa, T0):
    S = S0
    melhorSol = S
    melhorVal = fun(S)
    melhorIter = 0
    passo = (ls-li)/10.0
    T = T0
    j = 0
    random.seed(1)
    while (j < maxIter):
        Si = Vizinho (S, li, ls, passo)
        delta = fun(Si) - fun(S)
        if delta <= 0 or random.uniform(0, 1) < math.exp(-delta/T):
            S = Si
            if fun(S) < melhorVal:
                melhorVal = fun(S)
                melhorSol = S
                melhorIter = j
        T = T * alfa
        j = j + 1
    return [melhorSol, melhorVal]

config = sys.stdin.readline().strip().split(' ')
config = [float(val) for val in config]
result = sa(objfun, *config)
print "%.5f %.5f" % (result[0], result[1])
