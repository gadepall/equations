import numpy as np
A = np.array([[9,3],[18,6]])
B = np.array([-12, -24])
A1 = np.array([9,18])
A2 = np.array([3,6])
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


            
