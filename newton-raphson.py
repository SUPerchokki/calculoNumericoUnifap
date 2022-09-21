# metodo de newton rapshon para encontrar raizes de uma função
# imports
import numpy as np
import matplotlib.pyplot as plt

#definindo a função
def f(x):
    func = np.cos(x) -2*x**3
    return func

#derivada da função
def der(x):
    func = -np.sin(x)-6*x**2
    return func

#limitando as interações para que o looop não rode eternamente
maxInter = 20 #maximo de interações
e = 1E-15 # erro
i = 0 # contador de interações
x0 = 1 # palpite inicial
xi_1 = x0 # primeira interacao
print(f'interacao {i} : raiz = {x0} erro = {f(x0)}')

#interagindo até alcancar ou o maixmo de interações ou o erro minimo
while abs(f(xi_1)) > e or i > maxInter:
    i += 1
    xi = xi_1-f(xi_1)/der(xi_1) # a Equação de Newton Raphson
    print(f' Iteracao {i} : raiz {xi} : erro = {f(xi)}')
    xi_1 = xi
    
#plotando no grafico
x_plot = np.linspace(-2,2,1000)
y_plot = f(x_plot)

fig = plt.figure()
plt.plot(x_plot, y_plot, c='blue')
plt.plot(xi, f(xi),c='red',marker='o',fillstyle='none')
plt.xlim([-2,2])
plt.ylim([-2,2])
plt.xlabel('x')
plt.ylabel('y')
plt.grid()
plt.show()