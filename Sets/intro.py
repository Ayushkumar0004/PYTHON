#Set=store multiple values in single variable
#unordered
myset1 = {"car","boat","train"}
myset2 = {1,2,3,4}
myset3 = {4,5,6,7}
output=myset2.union(myset3)
output2=myset2.intersection(myset3)
output3 = myset2.symmetric_difference(myset3)
print(output)
print(output2)
print(output3)
myset1.add("Moto")
myset1.update(myset2)
print(myset1)
# duplicates are not allowed
# unchangable/immutable
# non homogenous  
if "boat" in myset1:
    print("Yaa")  
else:
    print("No")
tuple1 = ("H","E","L","L","O")
for i in tuple1:
    print(i,end="")  
     