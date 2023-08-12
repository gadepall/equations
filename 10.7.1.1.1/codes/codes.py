import numpy as np
A = np.array([2,3])
B = np.array([4,1])
C = (B-A)**2
D = np.linalg.norm(C, 1)
E =D**0.5
print (E)
