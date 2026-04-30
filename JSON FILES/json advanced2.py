import json

class Student:
    def __init__(self, name):
        self.name = name
        self.grades = {}

    def add_grades(self, grades, subject):
        self.grades[subject] = grades

    def view_grades(self):
        print(self.name, "->", self.grades)

    #comnvert the object to a dictionary

    def to_dict(self):
        return {
            "name": self.name,
            "grades": self.grades
        }
    
    #create object from dictionary
    @classmethod
    def  from_dict(cls, data):
        student = cls(data["name"])
        student.grades =data.get("grades", {})
        return student

s1 = Student ("Frank")
s1.add_grades("Math", 90)
s1.add_grades("java", 84)

s2 = Student("Mary")
s2.add_grades("python", 93)

students = [s1, s2]

with open ("student3.json", "w") as file:#saving multiple students
    json.dump([student.to_dict() for student in students], file, indent =4)

#loading the list form json
with open ("student3.json", "r") as file:
    data_list = json.load(file)#loading ,ultiple students

#convert dictionaries into student objects
loaded_students = [Student.from_dict(data) for data in data_list]

for student in loaded_students:
    student.view_grades()
''''
object - dict -json
json - dict - object

support for multiple objects
clean reusable class design

'''