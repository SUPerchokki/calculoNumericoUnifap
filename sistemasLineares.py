from operator import inv
import numpy as np
from numpy.linalg import inv
from numpy.linalg import solve

#solucionar sistemas lineares de duas variaveis
A = np.array([[2,4,-5],[4,1,-5],[2,4,5]])
B = np.array([5,2,-1])

# primeiro passo é achar a inversa da A e multiplicar por B
#inversa = inv(A)
#x = np.matmul(inversa,B)

# da mesma forma é possivel resolver utilizando a função solve
x = solve(A,B)
print(x)
print(f'\nX => {x[0]}\n')
print(f'Y => {x[1]}')