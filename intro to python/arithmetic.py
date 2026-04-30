##num1 =int(input('enter first number ')) 
#num2 =int(input('enter secomd number ')) 
#result = num1 * num2
#print(result)##

birth_year = int (input("enter your birth year "))
age  = 2026 - birth_year
print('You are ' +str(age) + ' years old')

x = 9 
t = 8 
# for comprarrison we use < > == != >= <= 
# // - floor division 
#% - gives the remainder and ** gives power eg, ( a ** b )
# for logical operators we have 
    #and , or , not

price = 20
has_id =  True

print(price >=18 and has_id)
print(age< 18 or has_id)
print(not has_id)

num = int(input ("Enter number: "))

if num%2 == 0:
    print("even number ")
else:
    print("the number is odd")

print("sum = ", x+t)
print("product = ", x*t)