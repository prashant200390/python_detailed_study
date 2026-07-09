age = int(input("Enter the age of a person :"))

if(age>18):
    print("Person is adult and can vote.")
    if(age>60):
        print("Person is senior citizen and can get special treatment in public places and government offices .")
    else:
        print("Person is not senior citizen.")
elif(age<=0):
    print("You are entering an invalid age .")
else:
    print("Person is a child in view of government and can't vote.")