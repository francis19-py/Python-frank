#a nested loop is a loop inside another loop 
#mukltiplication table
rows = 3
columns = 5

for r in range (rows):
    for t in range(columns):
        print(f'({r}, {t})', end=" ")
    print()

    for r in range(8):
        for c in range(8):
            if (r + c) % 2 == 0:
                print("⬜", end=" ")
            else:
                print("⬛", end=" ")
        print()

letters = {
"A": [
[0,1,1,0],
[1,0,0,1],
[1,1,1,1],
[1,0,0,1],
[1,0,0,1]
],

"F": [
[1,1,1,1],
[1,0,0,0],
[1,1,1,0],
[1,0,0,0],
[1,0,0,0]
],

"R": [
[1,1,1,0],
[1,0,0,1],
[1,1,1,0],
[1,0,1,0],
[1,0,0,1]
],

"N": [
[1,0,0,1],
[1,1,0,1],
[1,0,1,1],
[1,0,0,1],
[1,0,0,1]
],

"K": [
[1,0,0,1],
[1,0,1,0],
[1,1,0,0],
[1,0,1,0],
[1,0,0,1]
]
} 
name = input("Enter your name: ").upper()
for row in range(5):              # 5 rows tall
    for char in name:             # go through each letter typed
        if char in letters:       # if we have its design
            for cell in letters[char][row]:
                if cell == 1:
                    print("*", end=" ")
                else:
                    print(" ", end=" ")
            print("  ", end=" ")  # space between letters
    print()

digits = {
"8": [
[1,1,1],
[1,0,1],
[1,1,1],
[1,0,1],
[1,1,1]
]
}
num = "8"

for row in range(5):              # height
    for cell in digits[num][row]: # one row of the number
        if cell == 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()    