count=0
def names_count(names):
    global count
    for i in names:
        l=len(i)
        if len(i)>5:
            count=count + 1
            print(i)
            print(count)
       
       
names =["Manjodh","Mohit","Aman","Sultaan","Ghuman","Mr dhatt","Ajay"]
names_count(names)        