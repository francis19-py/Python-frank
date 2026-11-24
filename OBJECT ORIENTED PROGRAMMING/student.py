import json
import math
import statistics

class Student:
    university = "cooperative university of kenya"
    

    def __init__(self, name, age, course):
        self.name =name
        self.age = age
        self.course = course


    def display_details(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Course: {self.course}")
        print(f"University: {self.university}")
        print()
    def change_course(self, new_course):
        self.course = new_course

student1 = Student("francis maina", 24, "computer science")
student2 = Student("leonard maina", 25, "mathematics")

student1.change_course("information technology")

student1.display_details()
student2.display_details()
