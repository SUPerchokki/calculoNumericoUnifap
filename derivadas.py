#programa que calcula dervidas utilizando python
import numpy as np
from sympy import *

x = symbols('x')
f = np.cos(x)-2*x**3
df = diff(f,x)
print(df)