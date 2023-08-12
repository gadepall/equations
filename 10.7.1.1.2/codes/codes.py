import numpy as np
A = np.array([-5,7])
B = np.array([-1,3])
C = (B-A)**2
D = np.linalg.norm(C, 1)
E =D**0.5
print (E)
