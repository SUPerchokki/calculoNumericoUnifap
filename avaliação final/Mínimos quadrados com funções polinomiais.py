#Jacó Barros
#Vanessa Amaral
#Maria Victória

import matplotlib.pyplot as plt
import numpy as np
# plotar gráfico do dados
x = [0,0.25,0.50,0.75,1]
y = [1,1.284, 1.6487, 2.117, 2.7183]

grau = 2 # a0,a1,a2 -> y = a0 +a1x +a2x^2

# montagem da matriz

def termo_independente(x,y,grau):
    soma = 0
    for i in range(0,len(x)):
        soma = soma +y[i]*np.power(x[i],grau)
    return soma

M = np.zeros((grau+1,grau+2))

for i in range(0,grau+1):
    for j in range(0, grau+1):
       M[i][j]= np.sum(np.power(x,i+j))    

## preenchendo os termos independentes
for i in range(0,grau+1):
    M[i][grau+1]=termo_independente(x,y,i)
print("Matriz M", M)

def triangular(A):
    n = len(A) # n equacoes e n variáveis
    for i in range(n):
        pivot = A[i][i]
        for j in range(i+1,n): # linhas
            m=-A[j][i]/pivot
            for k in range(i,n+1): #colunas
                A[j][k]=A[j][k]+m*A[i][k]
    return A

def substituicao(A):
    n = len(A)
    x = n*[0] #vetor de n zeros
    #x[n-1]=A[n-2][n-2]/A[n-1][n-1]
    for i in range(n-1,-1,-1):
        soma = 0
        #substituir variável i
        for j in range(i+1,n):
            soma =  soma + A[i][j]*x[j]
        x[i]= (A[i][n] -soma)/A[i][i]  
    return x    


 
res = substituicao(triangular(M))
print("Solução:", res)


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