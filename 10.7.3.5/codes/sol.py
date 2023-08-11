import numpy as np
A = np.array(([4,-6])) 
B = np.array(([3,-2]))
C=  np.array(([5,2]))
m = 1
n = 1
P = ((m*C) + (n*B))/(m+n)
BP = P-B
BA = A-B
CP = P-C
CA = A-C
A1 = np.abs(0.5*(np.cross(BP,BA)))
A2 = np.abs(0.5*(np.cross(CP,CA)))
print(A1)
print(A2)
