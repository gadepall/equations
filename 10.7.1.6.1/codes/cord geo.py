import numpy as np
A = np.array([-1,-2])
B = np.array([1,0 ])
C = np.array([-1,2])
D = np.array([-3,-0])
print(A-B)
print(B-C)
print(C-D)
print(A-D)
print(A-C)
print(B-D)
print(D-C)
if  (A-B).all() == (D-C).all():
    print("It is parallelogram")
else:
    print("It is not a parallelogram")
if(((A-C).T)@(B-D)==0):
    print("It is a Rhombus")
else:
    print("It is not a rhymbous")
if(((A-B).T)@(B-C)==0):
    print("It is a rectangle")
else:
    print("It is not a rectangle")
if(((A-D).T)@(A-B)==0):
    print("It is a Square")
else:
    print("It is not a square")
