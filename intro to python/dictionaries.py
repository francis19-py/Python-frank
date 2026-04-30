#dictionary store data in key-value pairs
#these are like enumerations in cpp-- storing data that is related to one another
student= {
    "name": "Frank", 
    "age": 20,
    "course": "java"
    }
#eg name is the key while Frank is the value
print(student["name"])

#looping through a dictionary
for key in student:
    print(key, "->", student[key])
print()
#another way is using .items()
for key, value in student.items():
    print(key, "=", value)


#functions plus dictionaries

def print_info( dict_info):
    for key, value in student.items():
        print(key, ":", value)

print_info(student)

print()
def add_grade(student, subject, grade):
    if "grades" not in student:
        student["grades"] = {}   # create sub-dictionary if missing
    student["grades"][subject] = grade

add_grade(student, "Math", 90)
add_grade(student, "Python", 95)

print(student)

print()

#list contsining dictionaries
studentss = [
    {"name": "Frank", "age": 20},
    {"name": "Alice", "age": 22},
    {"name": "Brian", "age": 19}
]

print("name  age")
print("-------------------")
for studentt in studentss:
    print(studentt["name"], studentt["age"])



#add grades ti each student
def add_grades(studentss, subject, grade):
    if "grades" not in studentss:
        studentss["grade"] ={}
    studentss["grade"][subject]  =grade


add_grades(studentt[0], "math", 90)
add_grades(studentt[1], "math", 89)
add_grades(studentt[2], "math", 78)
        