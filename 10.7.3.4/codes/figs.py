#Python libraries for math and graphics
import numpy as np
import matplotlib.pyplot as plt
from numpy import linalg as LA 
import math

  
#Two aray vectors are given  
A = np.array(([-4,-2])) 
B = np.array(([-3,-5]))
C=  np.array(([3,-2]))
D=  np.array(([2,3]))


def line_gen(A,B):
   len =10
   dim = A.shape[0]
   x_AB = np.zeros((dim,len))
   lam_1 = np.linspace(0,1,len)
   for i in range(len):
     temp1 = A + lam_1[i]*(B-A)
     x_AB[:,i]= temp1.T
   return x_AB

#
#Generating all lines
x_AB = line_gen(A,B)
x_BC= line_gen(B,C)
x_CD= line_gen(C,D)
x_DA= line_gen(D,A)
x_AC= line_gen(A,C)


plt.plot(x_AB[0,:],x_AB[1,:])
plt.plot(x_BC[0,:],x_BC[1,:])
plt.plot(x_CD[0,:],x_CD[1,:])
plt.plot(x_DA[0,:],x_DA[1,:])
plt.plot(x_AC[0,:],x_AC[1,:])

#Labelling the coordinates
tri_coords = np.vstack((A,B,C,D)).T
plt.scatter(tri_coords[0,:], tri_coords[1,:])
vert_labels= ['A(-4,-2)','B(-3,-5)','C(3,-2)','D(2,3)']
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
plt.title("Area of quadrilateral ABCD")
plt.show()
