import numpy as np
A=np.array([[4/3,2],[2,3]])
A_1=[4/3,2]
A_2=[2,3]
B=[8,12]
B=np.array([8,12])
det_A=np.linalg.det(A)
x_num=[B,A_2]
y_num=[A_1,B]
if det_A!= 0:
     print("consistent")
     y=np.linalg.solve(A,B)
     print(y)
else:
    if(np.linalg.det(x_num)==0 and np.linalg.det(y_num)==0):
        print("consistent")
    else:
        print("inconsistent")
