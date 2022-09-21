import numpy as np

M = np.array([[2,-1,1],[1,2,3]])
# matriz F
n = len(M)
F= np.zeros((n,n))
for i in range(0,n,1):
    for j in range(0,n,1):
        if i==j:
            F[i][j]=0
        else:
            F[i][j]=-M[i][j]/M[i][i]
#print(F)
d = np.zeros(n)
for i in range(0,n,1):
    d[i]=M[i][n]/M[i][i]
#print(d)
#x_int = np.zeros(n)
x = np.zeros(n)
e = 10
i = 0
epslon = 0.01
while e >= epslon:
    i = i+1
    erro = x
    x = F.dot(x) + d  
    e = np.abs(np.max(erro) - np.max(x))
    print("iteração ",i ,": ", x)
    print("erro ",i ,":", e)                        
    if i > 100:
        break