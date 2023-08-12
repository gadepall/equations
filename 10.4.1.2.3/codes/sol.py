import numpy as np 
a =1
b =32
c =-273
#d=b*b-4*a*c  
d = (b*b) - (4*a*c)  
x1= (-b+np.sqrt(d))/(2*a)
x2 = (-b-np.sqrt(d))/(2*a)

print(x1.real)
print(x2.real)
