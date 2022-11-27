#Packing a tuple
tuple1 = (1,2,3)
(one, two, three) = tuple1
print(one)
print(two)
print(three)
tuple1 = (10,20,30,40)
for i in tuple1:
    print(i)
l = len(tuple1)
chr = 0
while l!=0:
    print(tuple1[chr])
    l = l-1
    chr+=1
