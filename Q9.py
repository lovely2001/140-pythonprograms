#python program to solve quadratic equation

import math
a = int(input("Enter coefficient of a : "))
b = int(input("Enter coefficient of b : "))
c = int(input("Enter coefficient of c : "))

discriminant = b**2 - 4*a*c

if discriminant>0:
    root1 = (-b+math.sqrt(discriminant))/(2*a)
    root2 = (-b+math.sqrt(discriminant))/(2*a)
    print("root1 : ", root1)
    print("root2 : ", root2)

elif discriminant==0:
    root = (-b)/(2*a)
    print("root : ", root)

else:
    realpart = -b/(2*a)
    imaginarypart = math.sqrt(abs(discriminant))/(2*a)
    print(f"root 1 : {realpart} + {imaginarypart}i")
    print(f"root 2 : {realpart} - {imaginarypart}i")

