import numpy as np 
A = np.array([3,0])
B = np.array([4,5])
C = np.array([-1,4])
D = np.array([-2,-1])
x=(1/2)*np.linalg.norm((np.cross(A-B,A-D)))
y=(1/2)*np.linalg.norm((np.cross(B-C,B-D)))
print ("Area of quadrilateral ABCD is", x+y)

