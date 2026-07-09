# write a program to convert inches into cm .
def convert(inches):
    cm = inches * 2.54
    print(f"{inches} inches is {cm} centimeter.")

i = float(input("Enter the value of i : "))
convert(i)