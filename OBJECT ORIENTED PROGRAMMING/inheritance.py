'''
Inheritance allows one class to reuse attributes and methods from another class.


'''
class person:
    def __init__(self, name,age):
        self.name = name
        self.age = age


class Student(person):
    def __init__(self, name, age, course):
        super().__init__(name, age)#This calls the parent class's constructor, allowing the child class to reuse its initialization logic.
        self.course = course

    def display_details(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Course: {self.course}")
        
student1 = Student("Frank", 24, "computer science")
student1 = Student("Leon", 25, "mathematics")

student1.display_details()
