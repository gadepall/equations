import numpy as np 
A = np.array([-2,2])
B = np.array([2,8])
k=1
C=(A+k*B)/(k+1)
print(C)
D=(A+k*C)/(k+1)
print(D)
E=(C+k*B)/(k+1)
print(E)