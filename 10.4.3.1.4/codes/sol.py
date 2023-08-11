import cmath  
a = 2
b = 1
c = 4
 
#calculate the discriminant  
d = (b*b) - (4*a*c)  
if d<0:
   print("Roots don't exist")
else:
#find two solutions  
  sol1 = (-b- cmath.sqrt(d))/(2*a)  
  sol2 = (-b+ cmath.sqrt(d))/(2*a)  

  print(sol1.real, sol2.real)
