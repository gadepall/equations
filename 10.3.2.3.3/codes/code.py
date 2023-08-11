import numpy as np
A=np.array([[3/2,5/3],[9,-10]])
a1=np.array([3/2,9])
a2=np.array([5/3,-10])
B=np.array([7,14])
det_A=np.linalg.det(A)
x_num=[B,a1]
y_num=[a1,B]
if det_A!=0:
  print("unique sol")
  x=np.linalg.solve(A,B)
  print(x)
else:
  if(np.linalg.det(x_num)==0 and np.linalg.det(y_num)==0):
     print("infinite")
  else: print("no sol")