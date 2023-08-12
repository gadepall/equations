import numpy as np
A = np.array([[2,1],[4,-2]])
A_1 = [2,4]
A_2 = [1,-2]
b=[6,4]
b = np.array([6,4])
det_A = np.linalg.det(A)
x_num = [b,A_2]
y_num = [A_1,b]
if det_A!= 0:
    print("unique solution")
    y = np.linalg.solve(A,b)
    print(y)
else:
    if(np.linalg.det(x_num)==0 and np.linalg.det(y_num)==0):
     print("infinite")
    else:
      print("no solution")

