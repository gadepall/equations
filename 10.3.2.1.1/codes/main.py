import numpy as np
A=np.array([[1,-1],[1,1]])
det_A= np.linalg.det(A)
b=np.array([4,10])
a1=np.array([1,1])
a2=np.array([-1,1])
x_num=[b,a1]
y_num=[a1,b]
if det_A != 0:
    print("unique solution")
    y=np.linalg.solve(A,b)
    print(y)
else:
    if(np.linalg.det(x_num) == 0 and np.linalg.det(y_num) == 0):
        print("infinite")
    else:
        print("no solution")
