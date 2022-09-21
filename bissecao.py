import numpy as np
# função cuja raiz será determinada
def f(x):
    return x*np.cosh(d)

#intervalo 
a = -2
b = 0
eps = 0.00000001 # erro
N = 30 # maximo iterações
fa = f(a)
fb = f(b)
k = 0
while ((b-a)>= eps or k > N):
    x = (a+b)/2
    if (fa*fb<0):
        b = x
        fb = f(x)
    else:
        a = x
        fa = f(x)
    k = k+1
    print("iteração: ",k, ", x: ",x, ", erro: ", b -a)
            


