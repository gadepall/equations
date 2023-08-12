import numpy as np
A = np.array(([1,5])) 
B = np.array(([2,3]))
C=  np.array(([-2,-11]))

AB = B-A
AC = C-A
Area = (0.5)*(np.cross(AB,AC))
if Area == 0:
   print("The points are collinear.")
else:
   print("The points aren't collinear.")
