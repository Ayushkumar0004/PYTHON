#companywill give bonus based on following criteria
#time spent in company             bonus
# < 10 years                        10%
# >6 and <10                        8%
# >6                                5%

#ask the salary and time spent from the user
#print the net bonus amount accordingly

serviceYears=int(input("how many years employee with the company:"))
salary=(input("current salary"))
bonus=("salary*0.1")

if serviceYears > 10 and serviceYears < 100:
    print("net bonus salary is:",bonus)
elif serviceYears <= 6 and serviceYears >= 10:
    print("net bonus salary is:",bonus)
elif serviceYears < 6:
    print("net bonus salary is:",bonus)         
else:
    print("invalid input:")