import numpy as np 
A = np.array(([-4,-2])) 
B = np.array(([-3,-5]))
C=  np.array(([3,-2]))
D=  np.array(([2,3]))



a1 = np.abs(0.5*np.cross(A-B,C-B))
a2 = np.abs(0.5*np.cross(A-D,C-D))
print("Area:",a1+a2)
