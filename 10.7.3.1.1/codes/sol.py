import numpy as np 
A = np.array([2,3])
B = np.array([-1,0])
C = np.array([2,-4])

AB = B - A
BC = C - B

Area = 0.5*np.cross(AB,BC)

print(Area)
