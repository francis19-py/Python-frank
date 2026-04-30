import math

def greet(name):
    print("hello there", name )

greet("Frank")
greet("mark")
greet ("Allan")
print()

def add (a,b):
    print(a +b)

add(3, 6)

def square(num):
    print(math.pow(num, 2))

square(8)


def add(g , f):
    return g + f

result = add(5, 3)
print("Result is", result)

def is_adult(age):
    return age >=18
print()
print(is_adult(34))
print(is_adult(10))

def cube(num):
    return math.pow(num, 3)

for i in range(2, 5):
    print("results for ", i, "=", cube(i))
