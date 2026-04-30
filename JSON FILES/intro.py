import json
student  = {
    "name" : "Frank",
    "age": 20,
    "grades": {
        "math": 90,
        "java": 92
    }
}

with open("student.json","w") as file:
    json.dump(student, file)#means dump this dictionary into the file

with open("student.json", "r") as file:
    data = json.load(file)

print(data)
print(data["grades"]["math"])
#json.load ()converts the file back into a dictionary