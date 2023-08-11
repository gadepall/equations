import numpy as np
A = np.array([[1,1],[2,-3]])
B = np.array([5, 4])
A1 = np.array([1,2])
A2 = np.array([2,-3])
det_A = np.linalg.det(A)
X_num = np.array([B, A2])
Y_num = np.array([A1, B])
if det_A!=0:
      print("unique solution")
else:
      if(np.linalg.det(X_num)==0 and np.linalg.det(Y_num)==0):
           {print("infinite")}
      else:
            print("no solution")

