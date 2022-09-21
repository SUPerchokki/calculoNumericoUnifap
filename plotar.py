import matplotlib.pyplot as plt
import numpy as np 
# plotar gráfico do sen(x)
x = np.linspace(0, 4, 100)
y = x*np.log10(x)-1
plt.plot(x,y)
plt.xlabel("valores de x")
plt.ylabel("f(x)")
plt.title("Gráfico de sen(x)")
plt.grid()
plt.show()





