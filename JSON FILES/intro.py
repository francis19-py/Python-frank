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
1. storing data in a file is called serialization
    student = {
    "name": "Frank",
    "age": 21,
    "course": "Computer Science"
    }
     save it as json
     import json

    with open("student.json", "w") as file:
      json.dump(student, file, indent=4)

      THE FILE 
        
      {
        "name": "Frank",
        "age": 21,
        "course": "Computer Science"
      }

2. reading JSON data into python
           {
    "name": "Frank",
    "age": 21,
    "course": "Computer Science"
    }

    THE BASIC RELATIONSHIP 
      Python Dictionary
       ↓
     json.dump()
        ↓
     JSON File
        ↓
        json.load()
        ↓
        Python Dictionary

3. JSON and APIs
  Important for backend develpment 
  for exapmple , a frontend might send 
        {
    "username": "frank",
    "email": "frank@example.com"
    }

    python backend can receive this data and convert it into a dictionary using json.load() and then process it accordingly.
    {
    "message": "User created successfully"
}
Frameworks such as Flask and FastAPI commonly work with JSON when building REST APIs.

4. JSON VS PYTHON

    JSON              Python
--------------------------------
    object       →    dictionary
    array        →    list
    string       →    str
    number       →    int/float
    true         →    True
    false        →    False
    null         →    None 

    


'''