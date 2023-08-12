import numpy as np 
import matplotlib.pyplot as plt 
from numpy import linalg as LA 
import math
from fractions import Fraction 

  
#Two aray vectors are given  
A = np.array(([-2,-2])) 
B = np.array(([2,-4])) 
m= 3
n=4
 
def find_n(point1,point2):
    P=np.array(point1)
    Q=np.array(point2)
#Formula for calculating the equidistance on x-axis  
    proj =  np.array((m*B+n*A)/(m+n))
    return proj
#Two aray vectors are given
point1 = np.array(([-2,-2])) 
point2 = np.array(([2,-4])) 

n=find_n(point1,point2)
print ('Line AB is divided in the ratio 3:4:', n)
 

 
def line_gen(P,Q): 
   len =10 
   dim = P.shape[0] 
   x_PQ = np.zeros((dim,len)) 
   lam_1 = np.linspace(0,1,len) 
   for i in range(len): 
     temp1 = P + lam_1[i]*(Q-P) 
     x_PQ[:,i]= temp1.T 
   return x_PQ 
 
   
x_AB = line_gen(A,B) 

 
 
 
 
#Plotting all lines 
plt.plot(x_AB[0,:],x_AB[1,:]) 
 
 
 
 
#Labeling the coordinates 
tri_coords = np.vstack((A,B,n)).T 
plt.scatter(tri_coords[0,:], tri_coords[1,:]) 
vert_labels = ['A','B','P'] 
for i, txt in enumerate(vert_labels): 
    plt.annotate(txt, # this is the text 
                 (tri_coords[0,i], tri_coords[1,i]), # this is the point to label 
                 textcoords="offset points", # how to position the text 
                 xytext=(10,-2), # distance from text to points (x,y) 
                 ha='center') # horizontal alignment can be left, right or center 
 
plt.xlabel('$x$') 
plt.ylabel('$y$') 
#plt.legend(loc='best') 
plt.grid() # minor 
plt.axis('equal') 
plt.title('Line segment AB',size=12) 

#if using termux

#else
plt.show()
