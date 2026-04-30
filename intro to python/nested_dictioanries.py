students = [
    {"name": "Frank", "age": 20},
    {"name": "Alice", "age": 22},
    {"name": "Brian", "age": 19}
]
for student in students:
    print(student["name"], student["age"])
print()

def add_grade(student, subject, grade):
    if "grades" not in student:
        student["grades"] = {}
    student["grades"][subject] = grade


add_grade(students[0], "Math", 90)
add_grade(students[1], "Math", 85)
add_grade(students[2], "Math", 70)


for student in students:
    print(student["name"], student["grades"]["Math"])
