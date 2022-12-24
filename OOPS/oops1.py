class student:
    numOfSubjects = 5
    def __init__(self,marks1,marks2,marks3):
        self.web = marks1
        self.python = marks2
        self.math = marks3
        
    def avg(self):
        print("The average marks are: ",(self.web+self.python+self.math)//3)    

    def getmarks(self):
        return self.math                    #Accessors

    def setmarks(self,marks):
        self.math = marks                    #Mutators
    @classmethod    
    def classMethodclass(cls):
        return student.numOfSubjects  
    def staticMethodclass():
        print("This is an example of satic method")      
student1 = student(5,6,4)
student2 = student(4,7,8)
student3 = student(8,7,5)
student1.avg()
student2.avg()
student3.avg()
print(student.classMethodclass())
student.staticMethodExample()
        