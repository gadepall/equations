import numpy as np
a=2
b=-14
c=-120
#d=b*b-4*a*cx2 = (-b-np.sqrt(d))/(2*a) 
d = (b*b) - (4*a*c)
x2 = (-b-np.sqrt(d))/(2*a) 
x1 = (-b+np.sqrt(d))/(2*a)  
print(x1.real) 
print(x2.real)
