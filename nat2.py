def Newton(f, dfdx, x, txErro):
    x1 = f(x)
    contaInter = 0
    while abs(x1) > txErro and contaInter < 100:
        x = x - float(x1)/dfdx(x)
        x1 = f(x)
        contaInter += 1
    if abs(x1) > txErro:
        contaInter = -1
    print(abs(x1))
    return x, contaInter

def f(x):
    return x**2 - 2

def dfdx(x):
    return 2*x

print("%.6f, %.1f" % Newton(f, dfdx, x=1000, txErro=1.0e-6))
