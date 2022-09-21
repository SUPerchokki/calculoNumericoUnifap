from operator import inv
import numpy as np
from numpy.linalg import inv
from numpy.linalg import solve

#solucionar sistemas lineares de duas variaveis
A = np.array([[10,3,4],[6,12,3],[6,5,17]])
B = np.array([280,390,670])

# primeiro passo é achar a inversa da A e multiplicar por B
#inversa = inv(A)
#x = np.matmul(inversa,B)

# da mesma forma é possivel resolver utilizando a função solve
x = solve(A,B)
print(x)
print(f'\nproduto 1 => {x[0]}\n')
print(f'produto 2 {x[1]}')
print(f'\nproduto 3 => {x[2]}\n')