import mymath

print(mymath.add(2, 4))
print(mymath.multiply(4, 6))

#importing a specific function 

from mymath import add

print (add(6,7))

#renaming a module 
import mymath as mm
print(mm.add(5, 6))