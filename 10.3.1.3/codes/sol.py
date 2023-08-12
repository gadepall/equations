import numpy as np
A=np.array([[1,-3],[1,-7]])
a1=np.array([1,1])
a2=np.array([-3,-7])
B=np.array([6,-42])
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
