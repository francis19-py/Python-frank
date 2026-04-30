#json does not understand classes, only understands dictionaries, lists, numberes, booleans, null
#Therefore we convert object into a dictionary, save the dictionary, load the dictionary then convert dictionary back into a student object
#The last step , from_dict() does that

import json #allows json to dump and load the dictionary
class Student:
    def __init__(self, name):
        self.name =name
        self.grades ={}

    def add_grades(self ,grade, subject):
        self.grades[subject] = grade

    def view_grades(self):
        print(self.name, "->", self.grades)


    
    @classmethod #special methid belonging to the class , not the object
    def from_dict(cls, data):
        student = cls(data["name"])#calls the constructor to make a new object
        student.grades = data.get("grades",{})
        return student
#cls refers to the student class itself
#data.get("grades",{}) - ensures it doesn't crash if no grades are existing, returns the fully recreated student object

s1 = Student("Frank")
s1.add_grade("Math", 90)
s1.add_grade("Python", 92)

with open ("student2.json", "w") as file:
    json.dump({"name": s1.name, "grades": s1.grades}, file, indent=4)

with open ("student2.json", "r") as file:
    data = json.load(file)

#automatically recreate object
s2 = Student.from_dict(data)

s2.view_grades()
    