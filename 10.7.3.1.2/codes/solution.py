import numpy as np 
A = np.array([-5,-1])
B = np.array([3,-5])
C = np.array([5,2])

AB = B - A
BC = C - B

Area = 0.5*np.cross(AB,BC)

print(Area)
