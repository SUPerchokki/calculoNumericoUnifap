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