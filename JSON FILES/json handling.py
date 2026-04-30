import json
import os

file_name = "student1.json"

if os.path.exists(file_name):
    with open (file_name, "rbU") as file:
        try:
            student1 = json.load(file) 
        except json.JSONDecodeError:
            student1 =[]
else:
    student1 =[] 

def save_data():
    with  open (file_name, "w") as file:
        json.dump(student1, file, indent =4)