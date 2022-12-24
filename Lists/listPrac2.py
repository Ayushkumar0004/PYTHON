num = [1,2,3,4,5,2,6]
number=[]
count=0
for x in num:
    if x==2 and count==0:
        x=200
        number.append(x)
        count+=1
    else:number.append(x)
print(number)        

