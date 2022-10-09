#a company decided to give bonus of 1000Rs to
#employee if his/her service is more than 5 yrs
#Ask user their salary and year of service and print
#the net bonus amount

yearsofemployee=float(input("how many yrs of service have you provided to this company? "))
salary=float(input("what is the current salary?"))

if yearsofemployee > 5:
    bonus=salary+1000
    print("your net bonus salary is:",bonus)

else:
    print("your net bonus salary is:",salary)
  
