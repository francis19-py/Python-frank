age = int(input("enter your age: "))
has_id = input ("Do you have an id? (yes /no): ")

if age >=18:
    if has_id =="yes":
        print("access granted")
    else:
        print("no id no access ! RUDI NYUMBANI")
else:
    print("you are underage for the event")
                