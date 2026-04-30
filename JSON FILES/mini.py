import json

name = input("what is your name? ")
age = int(input("Enter your age: "))

user = {
    "name": name,
    "age": age
}

with open ("studez.json", "w") as file:
    json.dump(user, file)

with open ("studez.json", "r") as file:
    data1 = json.load(file)

print("welcome", data1["name"] + "  age", data1["age"])