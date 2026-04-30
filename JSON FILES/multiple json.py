#instead of {}{} we store data as a list containing multiple dictionaries
import json
import os
file_name = "users.json"

#checking if file exists
if os.path.exists(file_name):
    with open(file_name, "r") as file:
        try:
            users = json.load(file)
        except json.JSONDecodeError:
            users = []
else:
    users = []

name = input("enter name: ")
age = int(input("Enter your age: "))

new_user = {
    "name" :name,
    "age" : age
}

#add user to list

users.append(new_user)

#save back to file 
with open (file_name, "w") as file:
    json.dump(users, file, indent=4)

print("user successfully saved")
