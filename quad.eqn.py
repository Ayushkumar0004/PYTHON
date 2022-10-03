import cmath

#a,b,c are all real numbers
#a!=0

a=int(input("enter the first number:"))
b=int(input("enter the second number:"))
c=int(input("enter the third number:"))
#formula of discriminant

d=(b**2-4*a*c)
#d=discriminant
root1=(-b-cmath.sqrt(d)/(2*a))
root2=(-b-cmath.sqrt(d)/(2*a))

print("the roots are",root1 ,"and",root2)
