#elif is short form of elseif
marks=int(input("Enter the marks"))

if marks > 90 and marks <= 100:
    print("YOUR GRADE IS A")

elif marks > 80 and marks <=90:
    print("YOUR GRADE IS B")

elif marks > 70 and marks <= 80:
    print("YOUR GRADE IS C")
    
else:print("not a valid number","enter the number between 0-100")    
 