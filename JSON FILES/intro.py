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
'''
1. storing python data in a json file
   student = {
    "name": "Frank",
    "age": 21,
    "course": "Computer Science"
}
save it a  json 
import json

    with open("student.json", "w") as file:
         json.dump(student, file, indent=4)
the file becomes:
    import json

with open("student.json", "w") as file:
    json.dump(student, file, indent=4)



2. reading the json file back into python
         import json

            with open("student.json", "r") as file:
                student = json.load(file)

        print(student["name"])

        
3. json and APIs
    imortant for backend development
    eg  a frontend might send a request to a backend server to get some data in json format

    




'''