#loop repeats code so you don't write it over and over
for i in range (5):#means from 0 ->4 thus five 
    print("hello")

    #range(1,6)-> means 1 to 5
    #range (2 , 10, 2)-> means looping through even values 2 4 6 8
for i in range(1, 11):
    print(i, "squared =", i * i)


#looping through a string

name = "frank"
for letter in name:
    print( letter)

total = 0
for i in range(101):
    total += i
print("sum = ", total) 

#unto while loops -- loop repeats while a condition is true

r =1
while r <=5:
    print(r)
    r += 1

#conditional loop -  runs iuntill a condition is met
password = ""
while password != "python":
    password = input("Enter password: ")

print("Access granted")

#guessing game
secret = 8

guess = 0
while guess != secret:
    guess = int (input ("Guess the secret number btwm 1 and 10: "))

print("your attempt is right")

#menu loop 
choice = ""

while choice != "q":
    print("Menu: (a) Add, (b) Subtract, (q) Quit")
    choice = input("Choose an option: ")

print("Goodbye 👋")   

#for countdown
count = 10

while count > 0:
    print(count)
    count -= 1

print("Blast off 🚀")

#for input validation
age = -1

while age < 0:
    age = int(input("Enter your age (positive number): "))

print("Your age is", age)