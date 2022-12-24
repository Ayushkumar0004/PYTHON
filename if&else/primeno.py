start_range=int(input("enter the first no: "))
end_range=int(input("enter the second no: "))
print("prime numbers in the range are:")
for number in range(start_range,end_range+1):
    if n > 1:
        for i in range(2,number):
            if (number%i)==0:
                break
else:
    print(number)            