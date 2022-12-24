#Make a program to detect our current attendance percentage
#total subjects
classAttended=float(input("how many classes have you attended?"))
attendencepercentage= (classAttended/125)*100
if attendencepercentage > 75:
 print("your attendence percentage is:", attendencepercentage,",you are eligible for exams")
else:
    print("your attendence is:", attendencepercentage,",you are not eligible for exams")


