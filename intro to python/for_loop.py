#for loo[p and tuples
students = [
    ("Alice ", 89),
    ("Mark", 90),
    ("Edward", 73)

]
print("{:<10} {}".format("Name","Score"))

for name , score in students:
    print(f"{name:<10}{score}")
    #print("{:<10}{}".format(name, score))

