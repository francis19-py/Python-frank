#default parameters

import math
def greet(name = "frank"):
    print("hello", name)

greet("mark")
greet()#default parameter is used 

#returning multiple valuesl

def calc(a, b):
    return a + b, a * b

sum, product = calc(4,5)
print( sum , product)

#keyword argument
print()
def student(name, age):
    print(name, age)

student(age = 23, name = "Frank")

#arbitrary arguments-- when you don't know the number of vslues 
del sum#restores built-in sum 
def total(*numbers):
    print(sum(numbers))

total(1, 2, 3)
total(10, 20, 30, 40)

def average_scores(*nums):
    if len(nums) == 0:
        print("No scores provided ")
        return
    avg = sum(nums) / len(nums)
    print("average: ", avg)

average_scores(45, 6,67,45)