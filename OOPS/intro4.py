
# a = "5"
# print(type(a))

# class Laptop:
#     def __init__(abc):
#         abc.name = 'ASUS'
#         abc.processor = 'i9'

#     def printOutput(abc):
#         print('My laptop name is: ', abc.name ,'My processor is: ', abc.processor)    

    # def config(self):
    #     print("ASUS","i7","1TB")
# laptop1 = Laptop()  
# laptop2 = Laptop() 
# laptop3 = Laptop() 
# laptop4 = Laptop() 

# # print(id(laptop1))
# # print(id(laptop2))
# laptop1.config()
# laptop2.config()
# laptop3.config()


# class person:
#     def __init__(self, name, rollno):
#         self.person = name
#         self.rollno = rollno

#     def printOutput(self):
#         print("My name is: ",self.person,"My roll no is: ",self.rollno)
# n1 = person("Ayush","10")
# n1.printOutput()
class person:
    def __init__(self):                                           #init is works automatically.it is a constructor.
        self.name = "Yash"
        self.age = 18
    def updateName(self):
        self.name = "Ayush"   
    def compareAge(self,other):
        if self.age == other.age:
            return True
        else:
            return False         

person1 = person()
person2 = person()
# person1.updateName("ABC")
# person2.name = "Atul"
person1.updateName()
person2.name="Onkar"
if person1.compareAge(person2):
    print("They are of same age")
else:
    print("The are of different age")    

print(person1.name,person1.age)
print(person2.name,person2.age)