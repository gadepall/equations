import numpy as np
A = np.array([-3, 5])
B = np.array([3,1])
C = np.array([0, 3])
D = np.array([-1, -4])
print(A-B)
print(B-C)
print(C-D)
print(A-D)
print(A-C)
print(B-D)
if(((A-B).T)@(D-C)==0):
    print("It is parallelogram")
else:
    print("it is not a parallelogram")    
if(((A-C).T)@(B-D)==0):
    print("Rhombus")
else:
    print("is is not a rhombus")
if(((A-D).T)@(A-B)==0):
    print("it is a Square")
else:
    print("it is not a square")
if(((A-B).T)@(B-C)==0):
    print("it is a rectangle")
else:
    print("it is not a rectangle")
