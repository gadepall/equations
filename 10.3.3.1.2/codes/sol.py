import numpy as np
A=np.array([[1,-1],[2,-3]])
det_A=np.linalg.det(A)
B=np.array([3,36])
a1=np.array([1,2])
a2=np.array([-1,-3])
x_num=[B,a2]
y_num=[a1,B]
if det_A != 0:
    print("unique solution")
    y=np.linalg.solve(A,B)
    print(y)
else:
    if(np.linalg.det(x_num) == 0 and np.linalg.det(y_num) == 0):
        print("infinite")
    else:
        print("no solution")
