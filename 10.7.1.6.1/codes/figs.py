import numpy as np
import matplotlib.pyplot as plt
from numpy import linalg as LA
import math

A = np.array([-1,-2])
B = np.array([1,0])
C = np.array([-1,2])
D = np.array([-3,0])

def linegen(A,B):
   len =2
   dim = A.shape[0]
   x_AB = np.zeros((dim,len))
   lam_1 = np.linspace(0,1,len)
   for i in range(len):
     temp1 = A + lam_1[i]*(B-A)
     x_AB[:,i]= temp1.T
   return x_AB

#Generating all lines
AB = linegen(A, B)
BC = linegen(B, C)
CD = linegen(C, D)
DA = linegen(D, A)

#Plotting all lines
plt.plot(AB[0,:],AB[1,:])
plt.plot(BC[0,:],BC[1,:])
plt.plot(CD[0,:],CD[1,:])
plt.plot(DA[0,:],DA[1,:])

#Labeling the coordinates
tri_coords = np.vstack((A,B,C,D)).T
plt.scatter(tri_coords[0,:], tri_coords[1,:])

plt.xlabel('$X-Axis$')
plt.ylabel('$Y-axis$')

plt.grid() # minor
plt.axis('equal')
plt.title('Quadrilateral',size=15)

plt.show()
