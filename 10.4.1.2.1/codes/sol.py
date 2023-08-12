import cmath  
a = 2
b = 1
c = -528  
d = (b*b) - (4*a*c)  
sol1 = (-b- cmath.sqrt(d))/(2*a)  
sol2 = (-b+ cmath.sqrt(d))/(2*a)  
print(sol1.real ,sol2.real)
e =  (2*sol2)+1
print(e.real)
