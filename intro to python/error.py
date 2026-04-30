#error hsndling --- try and except
try:
    num = int(input ("enter a number: "))
    result= (10/num)
except ZeroDivisionError:
    print("number can't be divide by zero")
except ValueError: 
    print("input a valid integer")

else:
    print("value calculated is:", result)


try:
    file = open("data.txt", "r")
except FileNotFoundError: 
    print("file is missing")
finally: 
    print("program  finished")



try:
    with open ("dats.txt","r") as file:
        print(file.read())
except FileNotFoundError:
    print("file does not exist")

try:
    num1 = int (input("Enter the firt number: "))
    num2 = int(input("Enter the second number: "))  
    result = num1/num2           
except ZeroDivisionError:
    print("Number can't be divided by zero")
except ValueError: 
    print("Number must be valid")
else:
    print("the result is : ", result)
