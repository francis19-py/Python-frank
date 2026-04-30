#anything inside quotes
#name = "Frank"
sentence = "i'm doing well"

#indexing , its like an array indexing , from zero onwards
word = "python"
print(word[2:5])
print(word[0])
print(word[:4]) #pyth
print(word[2:]) #thon

text = "python programming"

print(text.upper())       # PYTHON PROGRAMMING
print(text.lower())       # python programming
print(text.title())       # Python Programming
print(text.capitalize())  # Python programming



#checking if words exist
msg = "I love Python"

print("Python" in msg)   # True
print("Java" in msg)     # False

#replacing a word 
msg = "I like Java"
msg = msg.replace("Java", "Python")
print(msg)

#spliting text into list 
sentence = "apple banana mango"
fruits = sentence.split()

print(fruits)
#if to join , use . join()
words = ["I", "love", "Python"]
sentence = " ".join(words)

print(sentence)

#removing spaces
name = "   Frank   "
print(name.strip())
#string formatting


name = "Frank"
age = 20

#print("{} is  {} years old". format(name, age))

#print("{0} is  {1} years old. {0} loves football". format(name, age))

#print("{n} is {a} years old".format(n=name, a=age))


#modern  way

print(f"{name} is {age} years old")
print()

price = 9.99
quantity = 5
print(f" Total cost: ${ price *quantity:.2f}")

employee = "Markas"
employee_no = 201
marks = 400

print(f"{employee} has id number {employee_no} and has a total mark of {marks}")

name = (input("Enter your name: "))
age  = input("Enter your age: ")
city = input("Enter your city: ")

print(f" {name} is {age} years old and lives in {city} city ")