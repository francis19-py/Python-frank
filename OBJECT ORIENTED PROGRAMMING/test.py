class Student:
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course


    def display_details(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Course: {self.course}")

student1 = Student("frank", 34, "Data Structures")
student2 = Student("leon", 45, "Mathematics")

print("Student 1")
student1.display_details()

print()

print("Student 2")
student2.display_details()