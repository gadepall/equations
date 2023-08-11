import cmath

    
a = 100
b = -20
c = 1
      
# calculate the discriminant  
d = (b**2) - (4*a*c)  
      
# find two solutions  
sol1 =(-b-cmath.sqrt(d))/(2*a)  
sol2 =(-b+cmath.sqrt(d))/(2*a)  
    
#printing the results
print('roots are')
print(sol1.real)
print(sol2.real)
 
