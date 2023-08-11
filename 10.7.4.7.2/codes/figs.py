import numpy as np
import matplotlib.pyplot as plt
from numpy import linalg as LA

import sys

def line_gen(A,B):
    len=10
    dim = A.shape[0]
    x_AB = np.zeros((dim,len))
    lam_1 = np.linspace(0,1,len)
    for i in range(len):
        temp1 = A + lam_1[i]*(B-A)
        x_AB[:,i]= temp1.T
    return x_AB

A=np.array([4,2])
E=np.array([5,3.5])
F=np.array([2.5,3])


B=2*E-A
print("The vertex B is : ",B)

C=2*F-A
print("The vertex C is : ",C)

D=(B+C)/2

#Centroid=(A+B+C)/3
G=(A+B+C)/3
x_AB = line_gen(A,B)
x_BC = line_gen(C,B)
x_CA = line_gen(A,C)
x_EC = line_gen(E,C)
x_FB = line_gen(F,B)
x_AD = line_gen(D,A)

#Plotting all lines
plt.plot(x_AB[0,:],x_AB[1,:])
plt.plot(x_BC[0,:],x_BC[1,:])
plt.plot(x_CA[0,:],x_CA[1,:])
plt.plot(x_AD[0,:],x_AD[1,:])

#Labelling the coordinates
tri_coords = np.vstack((A,B,C,G,D
                        )).T
plt.scatter(tri_coords[0,:], tri_coords[1,:])
vert_labels= ['A(4,2)','B(6,5)','C(1,4)','p(3.6,3.6)','D(3.5,4.5)']
for i, txt in enumerate(vert_labels):
    plt.annotate(txt, #this is text
    (tri_coords[0,i], tri_coords[1,i]), #this is the point to label
    textcoords="offset points" , # How to position the text
    xytext=(0,10),#Distance from the text to points (x,y)
    ha='center') # horizontal alignment can be left , right or center
plt.xlabel("X")
plt.ylabel("Y")
#plt.legend(loc='best')
plt.grid()
plt.axis('equal')

plt.show()
