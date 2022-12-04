list1 = ["x","y","z"]
list2 = [1,2,3]

print(list1+list2)
for i in list2:
    list1.append(i)
print(list1)           