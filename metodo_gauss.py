

### resolucao sistemas lineares  ###
'''
Autor: Marcus Pantoja da Siva
Universidade Federal do Amapá
Eliminação de Gauss
'''
 
def triangular(A):
    n = len(A) # n equacoes e n variáveis
    for i in range(n):
        pivot = A[i][i]
        for j in range(i+1,n): # linhas
            m=-A[j][i]/pivot
            for k in range(i,n+1): #colunas
                A[j][k]=A[j][k]+m*A[i][k]
    print("Matriz triangular",A)
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



A = [[2,3,-1,5],[4,4,-3,3],[2,-3,1,-1]]
 
res = substituicao(triangular(A))
print("Solução:", res)


