class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
def display():
    print("NAME:",name)
    print("AGE",age)
    
class Student(Person):
    def __init__(Marks,Rollno):
        self.Marks=Marks
        self.Rollno=Rollno
        
    def displayinfo():
        print("MARKS",Marks)
        print("ROLLNO",Rollno)
        
        
        
        
        
        
        
        
        
        
        
        
    class Person:
        def __init__(self, name, age):
            self.name = name
            self.age = age

        def info(self):
            return f"Name: {self.name}, Age: {self.age}"


    class Student(Person):
        def __init__(self, name, age, roll_no, marks):
            super().__init__(name, age)          
            self.roll_no = roll_no               
            self.marks = marks

        def info(self):
            base = super().info()
            return f"{base}, Roll No: {self.roll_no}, Marks: {self.marks}"

        def get_grade(self):
            if self.marks >= 90:
                return "A"
            elif self.marks >= 80:
                return "B"
            elif self.marks >= 70:
                return "C"
            elif self.marks >= 60:
                return "D"
            else:
                return "F"


    if __name__ == "__main__":
        students = []                            

        print("=== Student Management System ===\n")
        num_students = int(input("Enter number of students: "))

        for i in range(num_students):
            print(f"\n--- Student {i + 1} ---")
            name = input("Enter name: ")
            age = int(input("Enter age: "))
            roll_no = input("Enter roll number: ")
            marks = float(input("Enter marks: "))

            student = Student(name, age, roll_no, marks)
            students.append(student)              

        print("\n=== Student Information ===\n")
        for student in students:
            print(student.info())
            print(f"Grade: {student.get_grade()}\n")
    