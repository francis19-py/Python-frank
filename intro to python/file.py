file = open("data.txt", "w")#opening a file
#filename followed by mode
# "r" read, w - write, a - append, x- create file 

#reading a file
file = open("data.txt", "r")
content = file.read() #reads everything
print(content)
file.close()

#reading line by line 
file = open("data.txt", "r")

for line in file:
    print(line)
file.close()

#writing to a file----deletes all contents 
file =open("data.txt", "w")

file.write("Hello there\n")
file.write("How are you ?")
file.close()

#append() just adds info to the file without deleting anything
#for auto,matic closing

with open("data.txt", "r") as file:
    contemt = file.read()
    print(content)

name = input("enter your name: ")

with open ("users.txt", "a") as file: 
    file.write(name + "\n")

print("saved")

print()

message= input("enter  your note: ")

with open ("name.txt", "a") as file:
    file.write( message + "\n")

with open ("name.txt", "r") as file:
    content= file.read()

print("all notes: ")
print(content)
