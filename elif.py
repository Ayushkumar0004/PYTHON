#user input three sides of triaangle
s1=int(input("enter the first side:"))
s2=int(input("enter the second side:"))
s3=int(input("enter the  third side:"))

if s1+s2 > s3:
    print("the triangle is possible")
else:
    print("the triangle is not possible")    