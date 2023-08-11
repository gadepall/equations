# import complex math module  
import cmath  
import numpy as np
a = np.sqrt(2)
b = 7
c = 5*(np.sqrt(2))
  
# calculate the discriminant  
d = (b*b) - (4*a*c)  
  
# find two solutions  
sol1 = (-b- cmath.sqrt(d))/(2*a)  
sol2 = (-b+ cmath.sqrt(d))/(2*a)  

print(sol1.real,sol2.real)   
