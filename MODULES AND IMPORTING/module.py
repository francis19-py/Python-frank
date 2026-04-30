# a module is a python file comntaining functions
#used in real, life projects
#there are built in modules such as 

name = input("Enter your namre: ")

try:
    age = int(input("enter ypur age: "))
except ValueError:
    print("invalid age. input an integer")
else:
    print(f"your name is", name, "and you are ", age, "years old")

    
