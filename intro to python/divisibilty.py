number = int(input("enter a random number : "))

if number % 3 ==0 and number % 5==0:
    print("the number is divisible by both 3 and 5") 
elif number % 3 == 0:
    print("the number is divisible by 3")
elif number % 5 == 0:
    print("the number is disible by 5")
else:
    print("the number is neither divisible by 3 or 5")