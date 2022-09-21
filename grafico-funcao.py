import matplotlib.pyplot as plt
import numpy as np

def pica(x):
    return (np.add(np.absolute(np.sin(x)) ,np.multiply(np.multiply(np.exp(-x ** 100), np.cos(x)), 5)))

x = np.linspace(-3.14,3.14,20000)
plt.plot(x, pica(x), 'o')
plt.grid()
plt.show()