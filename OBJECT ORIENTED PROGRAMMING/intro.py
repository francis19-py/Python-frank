#deals with creating entities 
#data plus the behaviour

#creating a class
class Student:
    def __init__(self, name):#_init__ is constructor
        self.name =name
        self.grades ={}

    def add_grade(self, subject, grade):
        self.grades[subject] = grade

    def view_grade(self):
        print(self.name, "->", self.grades )
#self - reffers tom the currrent student object
#self.name - stores the student name
#self.grades - empty dictinary for subjects

#creating an object 
s1 = Student("Frank")
s1.add_grade("Math", 90)
s1.add_grade("python", 92)

s1.view_grade()   


    
