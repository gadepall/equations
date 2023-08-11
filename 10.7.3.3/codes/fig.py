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

A=np.array([0,-1])
B=np.array([2,1])
C=np.array([0,3])
m= 1
n= 1
D = ((m*B) + (n*A))/(m+n)
E = ((m*C) + (n*B))/(m+n)
F = ((m*A) + (n*C))/(m+n)


x_AB = line_gen(A,B)
x_BC = line_gen(C,B)
x_CA = line_gen(A,C)
x_DE = line_gen(D,E)
x_DF = line_gen(D,F)
x_EF = line_gen(E,F)

#Plotting all lines
plt.plot(x_AB[0,:],x_AB[1,:])
plt.plot(x_BC[0,:],x_BC[1,:])
plt.plot(x_CA[0,:],x_CA[1,:])
plt.plot(x_DE[0,:],x_DE[1,:])
plt.plot(x_DF[0,:],x_DF[1,:])
plt.plot(x_EF[0,:],x_EF[1,:])

#Labelling the coordinates
tri_coords = np.vstack((A,B,C,D,E,F)).T
plt.scatter(tri_coords[0,:], tri_coords[1,:])
vert_labels= ['A(0,-1)','B(2,1)','C(0,3)','D(1,0)','E(1,2)','F(0,1)']
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
plt.title("Triangles ABC and DEF")
plt.show()
