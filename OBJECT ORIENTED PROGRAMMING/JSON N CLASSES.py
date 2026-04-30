import json

class Student:
    def __init__(self, name):
        self.name = name
        self.grades = {}

    def add_grades(self, subject, grade):
        self.grades[subject] = grade

    def view_grades(self):
        print(self.name, "->", self.grades)

s1 = Student("Frank")
s1.add_grades("math", 90)
s1.add_grades("python", 83)

#convert into a dictionary
student_dict = {
    "name" : s1.name,
    "grades" : s1.grades
}
#save to the json file
with open("data.json", "w") as file:
    json.dump(student_dict, file, indent=4)

with open("data.json", "r") as file:
    data = json.load(file)

#recreating object
s2= Student(data["name"])
s2.grades =data["grades"]

print(s2.name)
print(s2.grades)
