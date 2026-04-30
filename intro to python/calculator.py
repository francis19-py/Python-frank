num1 = float(input("Enter the first number:  "))
operator = input("enter the operand (/ * + - %): ")
num2 = float(input("enter the second number: "))

if operator == "+":
    print("result = ", num1 + num2)
elif operator == "-":
    print("result = ", num1 - num2)
elif operator == "/" and num2 != 0:
    print("result =  ", num1/num2)
elif operator == "*":
    print("result = ", num1 * num2)
elif operator == "%":
    print("result  = ", num1 % num2)
else:
    print('invalid operator')