a=float(input("enter the first no"))
b=float(input("enter the second no"))
c=float(input("enter the third no"))

p=a+b+c
s=p

area=s*(s-a)*(s-b)*(s-c)**0.5

print("perimeter of the triangle",p)
print("semi perimeter of the triangle",s)
print("area of the triangle",area)