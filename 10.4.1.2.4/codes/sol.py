import cmath  
a = 1
b = -8
c = -1280  
d = (b*b) - (4*a*c)  
sol1 = (-b- cmath.sqrt(d))/(2*a)  
sol2 = (-b+ cmath.sqrt(d))/(2*a)  
print(sol1.real ,sol2.real)
