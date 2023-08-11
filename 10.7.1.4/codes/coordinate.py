import numpy as np
A = np.array([5,-2])
B = np.array([6,4])
F = np.array([7,-2])
C = (B-A)**2
G = (F-B)**2
H = (F-A)**2
D = np.linalg.norm(C, 1)
I = (np.linalg.norm(G, 1))**(0.5)
J = (np.linalg.norm(H, 1))**(0.5)
E =D**0.5
print (E)
print (I)
print (J)


