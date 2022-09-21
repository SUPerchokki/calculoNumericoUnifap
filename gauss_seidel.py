import numpy as np
'''Método de Gaus de Seidel'''
M = np.array([[2,-1,1],
              [1,2,3]])
# ordem do sistema
n = len(M)
#solucao inicial
x =np.zeros(n)
#erro
epsilon = 0.01
#iteracoes
k = 10
# matriz F
F = np.zeros((n,n))
for i in range(0,n): # linha
    for j in range(0,n): # coluna
        if i==j:
            F[i][j]=0
        else:
            F[i][j]=-M[i][j]/M[i][i]    

# vetor d
d=np.zeros(n)
for i in range(0,n,1):
    d[i]=M[i][n]/M[i][i]
print(d)    
# método iterativo de Gauss-Seidel
i = 0
erro = 100
while erro >= epsilon:# critério de parada pelo erro
    i = i+1
    erro = np.max(x)
    for l in range(0,n): #linhas
        soma = 0
        for c in range(0,n): #colunas
            soma = soma + F[l][c]*x[c]
        x[l]= soma + d[l]
    erro = np.abs(erro - np.max(x))    
    print("iteração ",i, " x = ",x, "erro = ",erro)
    if i >= k: # critério de parada pelo número de iterações
        break

