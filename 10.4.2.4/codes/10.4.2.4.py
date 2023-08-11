import cmath 
a = 1
b = 1
c = -182
#calculate the dicriminant
d = (b*b)-(4*a*c)
#find two roots
sol1 = (-b-cmath.sqrt(d))/(2*a)
sol2 = (-b+cmath.sqrt(d))/(2*a)

print(sol1.real , sol2.real)
