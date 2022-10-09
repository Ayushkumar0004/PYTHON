#take input of age of three people
#determine the oldest and youngest

age1=int(input("enter the first people age:"))
age2=int(input("enter the second people age:"))
age3=int(input("enter the third people age:"))

if age1 > age2 and age1>age3:
    print("the oldest age is:",age1)
elif age2 > age1 and age2>age3:
    print("the oldest age is",age2)
elif age3>age1 and age3>age2:
    print("the oldest age is",age3)

if age1 < age2 and age1< age3:
    print("the youngest age is:",age1)
elif age2 < age1 and age2 < age3:
    print("the youngest guy is:",age2)
elif age3 < age1 and age3 < age2:
    print("the youngest age is:".age3)          

else:
    print("ALL ARE OF SAME AGE:")