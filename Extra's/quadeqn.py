import cmath
#a,b,c all are real number
#a!=0

a=int(input("enter the number (a!=0):"))
b=int(input("enter the number:"))
c=int(input("enter the number:"))
#formula for discriminant
d=(b**2-4*a*c)
#d=discriminant

root1=(-b-cmath.sqrt(d)/2*a)
root2=(-b+cmath.sqrt(d)/2*a)
print("the roots are", root1, "and" ,root2)