#take a user input if the length of that input is greater than 3 characters add ing as suffix else print the same input.
string=str(input("enter the word:"))
a=len(string)
b=("ing")
if a > 3:
    print(string+b)
else:
    print(string)    