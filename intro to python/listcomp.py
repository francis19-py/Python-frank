squares = []
 
for x in range(5):
    squares. append(x * x)

print(squares)

#the shortcut
squares = [x * x for x in range(5)]
print(squares)

evens = [x * x for x in range (10) if x % 2 ==0 ]
print (evens)

#the structure is :
   # [ expression for item in iterable if condition ]

names = ["Frank", "Ann", "Peter"]
lengths = [len(name) for name in names]
print(lengths)


list2 = [x for x in range(20) if x %3 == 0]
print(list2)