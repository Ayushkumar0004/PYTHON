# tuples-stores multiple items in a single variable 
# non homogenous
# ordered
# unchangable/immutable
# allows duplicate value

mytuple = (1,2,3,4,5,5)
print(len(mytuple))
print(mytuple)

tuple1 = ("apple",1,1.1)
print(tuple1)

tuple2 = ("car","bike","boat","jet")
print(tuple2[:3])
tuple2 = ("car","bike","boat","jet")
list1 = list(tuple2)
list1.append("cycle")
tuple3 = tuple(list1)
print(tuple3)
tuple4 = (10,20,30,40,50)
#reverse it
tuple4 = list(tuple4)
tuple4.sort(reverse=True)
tuple4 = tuple(tuple4)
print(tuple4)
tuple5 = ("AYUSH",)
print(tuple5)
tuple6 = ("apple","orange","pineapple")
del tuple6
print(tuple6)
tuple7=(1,2,3,[6,7],4,5)
tuple7[3][0]=8
print(tuple7)