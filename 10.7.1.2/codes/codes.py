import numpy as np
A = np.array([0,0])
B = np.array([36,15])
C = (B-A)**2
D = np.linalg.norm(C, 1)
E =D**0.5
print (E)
