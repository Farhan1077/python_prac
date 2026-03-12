class person:
    def __init__(self,name,age):
        print("inside Person Constructor")
        self.name = name
        self.age = age
        
class Student(person):
        def __init__(self,name,age,marks1,marks2,sem):
            person.__init__(self,name,age)
            self.sem = sem
            self.marks1 = marks1
            self.marks2 = marks2
            
        def avgmarks(self):
            total = self.marks1+self.marks2
            avg = total/2
            print("Average Marks :",avg)
            
        def getdata(self):
            print("name: ",self.name)
            print("Age: ",self.age)
            print("sem: ",self.sem)
            print("marks1: ",self.marks2)
            print("marks2: ",self.marks1)
            
        def __del__(self): 
            print("Object Destroyed! ")
        
        
x=Student(1,"Swayam",2,60,60) 
print(x.getdata()) 
print(x.avgmarks()) 
y = Student(2,"Swayam",1,80,90) 
y.getdata() 
y.avgmarks()
