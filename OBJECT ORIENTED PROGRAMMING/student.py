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
        print(f"University: {Student.university}")
        print()
    @classmethod
    def change_university(cls, new_university):
        cls.university = new_university

    @staticmethod
    def is_eligible(age):
        return age >= 18
students = []

frank = Student("francis maina", 24, "computer science")
leon = Student("leonard maina", 25, "mathematics")

print("before changing university: \n")
frank.display_details()
leon.display_details()

Student.change_university("univerty of Nairobi")

print("after changing university: \n")
frank.display_details()
leon.display_details()

print("\nEligibility check:")
print(f"Frank (age {frank.age}) eligible: {Student.is_eligible(frank.age)}")
print(f"Leon (age {leon.age}) eligible: {Student.is_eligible(leon.age)}")
