import matplotlib.pyplot as plt
import numpy as np 
# plotar gráfico do dados
x = [0,1,2,3]
y = [1,2,4,8]
plt.plot(x,y)
plt.xlabel("valores de x")
plt.ylabel("f(x)")
plt.title("Gráfico de f(x)")

# extrapolacao y = ax+b
# calculo de a e b
sfx = 0
sf = 0
sx = 0
sx2 = 0
n = len(x) #número de ponto


# implementar o metodo de gaus
# calculo dos minimos quadrados do polinomio
for i in range(0,n):
    sfx = sfx + y[i]*x[i]
    sf = sf + y[i]
    sx = sx + x[i]
    sx2 = sx2 + x[i]*x[i]
a = (n*sfx - sf*sx)/(n*sx2 - sx*sx)    
print(a)
b = (sx2*sf - sfx*sx)/(n*sx2-sx*sx)
print(b)
y2 = np.zeros(n)
for i in range(0,n):
    y2[i]=a*x[i]+b
plt.plot(x,y2)
plt.grid()
plt.show()

