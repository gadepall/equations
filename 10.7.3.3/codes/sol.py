import numpy as np
A=np.array([0,-1])
B=np.array([2,1])
C=np.array([0,3])

m= 1
n= 1
D = ((m*B) + (n*A))/(m+n)
E = ((m*C) + (n*B))/(m+n)
F = ((m*A) + (n*C))/(m+n)
a1 = (0.5)*(np.cross(B-A,C-A))
a2 = (0.5)*(np.cross(E-D,F-D))
print("The ratio of two triangles:",a2/a1)
