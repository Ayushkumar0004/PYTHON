serviceYears=int(input("enter the years of service:"))

salary=float(input("current salary:"))
bonus=(salary+5/100)

if serviceYears > 5:
    print("salary:",bonus)

else:
    print("NO bonus:")