#adding many objects using the class

import statistics
import json
class Student:    
    def __init__(self, name):
        self.name = name
        self.grades = {}


    def add_grades(self, subject, grade):

        self.grades[subject]= grade

    def get_average(self):
        if not self.grades:
             return 0
        return statistics.mean(self.grades.values())

    def view_grades(self):
        print(self.name, "->", self.grades, "| Average: ", self.get_average())

        
students = []#crsate a  list to multiple students

while True:
     print("\n1. Add student")
     print("2. Add grade")
     print("3. View student")
     print("4. Exit")


     choice = input("Enter the choice: ")

     if choice == "1":
          name = input("Enter the name of the student: ")
          new_student = Student(name)
          students.append(new_student)
          print("student added !")

     elif choice  == "2":
          name = input("Enter the name of student: ")

          for student in students:
            if student.name == name:
               
                subject = (input("Enter the subject: "))
                grade = int(input("eEnter the grade: "))
                student.add_grades(subject, grade)
                print("grades added successfully!")
                break
          else:
              print("Student not found")
     elif choice == "3":
          for student in students:
               student.view_grades()

     elif choice  == "4":
          break
     
     else:
          print("invalid choice!")

students_data =[student.__dict__ for student in students]#convert the list of objects into a list of dictionaries
with open ("data1.json", "w") as file:
    json.dump(students_data, file, indent=4)          



