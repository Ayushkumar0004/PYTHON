a=int(input("enter the first no"))
b=int(input("enter the second no"))
c=int(input("enter the third no"))

p=(a+b+c)
s=p/2

area=(s*(s-a)*(s-b)*(s-c))**0.5

print("area of the triangle:", area)