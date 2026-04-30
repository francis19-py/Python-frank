#simlilar to lists but with special behavior
#  a list that cannot change
numbers  = ( 1, 2, 3, 4)
names =  ("Frank", "Mark", "Eliud")
#in tuples we use parentheses  instead of brackets
#they are static hence once decclared they cannot be changed
#hence said to be immutable
# they are goid for coordinates, fixed data, settimgs

#accessed i same way as lists

print(names[0])
print()
#tuple unpacking 
person =("Frank", 20, "Nyeri")

name, age, county = person
print (name)
print(age)
print(county)

print()

#creating a set-- a collection that has nin duplicates and is unordered


nums = {1, 2, 3,4, 5}

name = { "Frank", "Mark", "Frank"}
print(name)#duplicates are ignored

#adding values
nums.add(9)
nums.remove(2)
print()
#set operations

a = {1, 2, 3}
b= {3, 4, 5}

print(a | b)#union
print(a & b)#intersection
print(a - b)#difference

#sets used when - removing duplicates, checking membership fast, comparing collections
list1 = [1, 2, 2, 3, 4, 4, 5]

unique_set = set(list1)#removes duplicates

new_list = list(unique_set)#converts back to list
new_list = sorted(list(unique_set))#add sort since sets are unordered
print(new_list)