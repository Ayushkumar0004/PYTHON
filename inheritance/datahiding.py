class person:
    def __init__(self,Name,age):
        self.__name = Name
        self.__age = age
    def getName(self):
        return self.__name
    def getAge(self):
        return self.__age 
person1 = person("Ayush",18) 
print(person1._person__name) 
       