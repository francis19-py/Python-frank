#student record 
import json
import os
file_name = "students.json"

if os.path.exists(file_name):
    with open(file_name, "r") as file:
        try:
            students = json.load(file)#studemts is a variable that holds data that was inside the json file
        except json.JSONDecodeError:
            students = []
else:
    students = []

#function to save data

def save_data():
    with open (file_name, "w") as file:
        json.dump(students, file, indent=4)

#addd/ update student

def add_student():
    name = input("Enter your name: ")
    subject = input("Enter the subject: ")
    grade  = int(input("Enter the grade: "))

    for student in students:
        if student["name"].lower() ==name.lower():
            student["grades"][subject] = grade
            save_data()
            print(f"{name}'s student data saved")
            return
        
    new_student = {
        "name": name,
        "grades": {
            subject: grade
        }
    }

    students.append(new_student)
    save_data()
    print(f"new student's {name} added!")

#search student function
def search_student():
    name = input("Enter student name to search: ")

    for student in students:
        if student["name"] == name:
            print(f"{name}'s grades: {student["grades"]}")
            return
        
    print("student not found")


def view_student():
    if not students:
        print("No record found")
        return
    for student in students:
        print(student["name"], "->", student["grades"])
        
def filter_students():
    subject = input("Enter the subject to filter: ")
    min_grade =int(input("Enter minimum grade: "))
    found = False

    for student in students :
        if subject in student["grades"]:
            if student["grades"][subject] >=min_grade:
                print(f"\n{student['name']} -> {subject}: {student['grades'][subject]}")
                found = True

    if not found:
        print(f"no students found with {subject} >= {min_grade} ")

while True:#ensures a comntinous loop
    print("\n1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Filter students by grade ")
    print("5. Exit")
    print()

    choice = input("Enter choice")
    print()
    if choice == "1":
        add_student()

    elif choice == "2":
        view_student()

    elif choice == "3":
        search_student()

    elif choice == "4":
        filter_students()
    elif choice == "5":
        break
    else:
        print("Invalid choice")