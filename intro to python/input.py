birth_year= input('Birth_year:' )
Age = 2026 - int(birth_year)
print ("You are "  + str(Age) + " years old")#the integer must be converted to string type to be printed out together
#print(type(Age))#shows the type of data


#printing out a course 
course = '''
hello there

I'm Francis

How may I help you today?
'''
hello = "hello there"
print (hello[-2])
print(hello[0:3])
#if you just put [0:], it'll print out all the variables

#formatted strings
word1 = 'Frank'
word2 = 'Mark'
message = word1  +" " + word2 +" is a programmer"
print (message)
methods ='''
Method	What it does	Example
lower()	All lowercase	"HELLO".lower() → "hello"
upper()	All uppercase	"hi".upper() → "HI"
title()	Capitalize each word	"hello world".title() → "Hello World"
capitalize()	First letter uppercase	"python".capitalize() → "Python"
swapcase()	Swap upper/lower	"PyThOn".swapcase() → "pYtHoN"
casefold()	Strong lowercase (for comparisons)	"ß".casefold() → "ss"
'''