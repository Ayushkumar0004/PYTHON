a=int(input("enter the first number"))
b=int(input("enter the second number"))
c=int(input("enter the third number"))

p=a+b+c
s=p/2

area=s*(s-a)*(s-b)*(s-c)**0.5


print("perimeter of triangle is:",p)
print("semi perimeter of triangle is:",s)
print("area of triangle is:",area)