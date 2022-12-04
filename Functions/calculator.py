def sum(user_input1,user_input2):
    sum=user_input1+user_input2
    print("The sum is:",sum)
def product(user_input1,user_input2):
    product=user_input1*user_input2  
    print("The product is:",product)
def diff(user_input1,user_input2):
    diff=user_input1-user_input2
    print("The difference is:",diff)
def div(user_input1,user_input2):
    div=user_input1/user_input2
    print("The div is:",div)    
user_input1=int(input("num1: "))
user_input2=int(input("num2: "))
op = input("Enter the operator from the list: +,-,/,*: ")
op_list = ["+","-","/","*"]
if op in op_list:
    if op =="+":print(sum(user_input1,user_input2))
    elif op=="-":print(diff(user_input1,user_input2))
    elif op=="/":print(div(user_input1,user_input2))
    elif op=="*":print(product(user_input1,user_input2))
else:print("INVALID INPUT")
     