import numpy as np

def resol(A,b):
    n = len(b)
    x = [0]*n
    x[n-1] = b[n-1]/A[n-1][n-1]
    for i in range(n-1,0,-1):
        s = 0
        for j in range(i+1,n+1,1):
            s = s + A[i-1][j-1]*x[j-1]
        x[i-1] = (b[i-1]-s)/([A[i-1][i-1]])
    return x
A = np.array([[3, 2, 4],
     [0, (1/3), (2/3)],
     [0,0,-8]])
b = np.array([1, (5/3), 0])

x = resol(A,b)
print('x = ', x)
