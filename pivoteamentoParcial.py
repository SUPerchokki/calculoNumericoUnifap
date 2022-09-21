import numpy as np
M = np.array([[2,3,-1,5],[4,4,-3,3],[2,-3,1,-1]])
# dimensao da matriz M

def pivoteamento_parcial(M):
    for k in range(n-1):
        if np.fabs(M[k,k]) < 1.0e-12:
            for i in range(k+1, n):
                if np.fabs(M[i,k]) > np.fabs(M[k,k]):
                    M[[k,i]] = M[[i,k]]
    for i in range(k+1,n):
        if M[i,k] == 0:continue

        fat = M[k,k]/M[i,k]
        for j in range(k,n):
            M[i,j] = M[k,j] - M[i,j]*fat
    print(M)
    return M

n = len(M)
for j in range(0,n,1): # coluna 0 até coluna n-1
    M = pivoteamento_parcial(M)
    pivot = M[j][j] # pivot da coluna
    for i in range(j+1,n,1): #linhas
        m=-M[i][j]/pivot
        M[i][:]=m*M[j][:]+M[i][:]                
    #print(M)    
x = np.zeros(n)

for j in range(n-1,-1,-1):
    soma = 0
    for i in range(j+1,n,1):
        soma = soma + M[j][i]*x[i] 
    x[j]=(M[j][n]-soma)/M[j][j] 
print("O vetor solução é: ",x)
