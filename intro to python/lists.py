fruits = ["mango", "apple", "passion"]

print(fruits[0])

#looping through a list
for i in fruits:
    print(i)
print()
#functions plus lists
def print_info(car):
    for i in car:
        print(i)
    
cars = ["maserati", "bmw", "corvette"]
print_info(cars)

print()

def cube_list(numbers):
    cube = []
    for num in numbers:
        cube.append(num **3)
    return cube

integer = [4, 5, 8, 9]
print(cube_list(integer))