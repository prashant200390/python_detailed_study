def convert(c):
    f = (c * 1.8 + 32) # or we can just , f = (c * (9/5) + 32)
    print(f"{c} celsius is {f} fahrenite.")
c = float(input("Enter the value of celsius to convert : "))

convert(c)

def convert_to_celsius(f):
    c = ((f-32)/9) * 5
    return round(c,2)

f = float(input("Enter the value of fahrenite to convert : "))
print(f"{f} fahrenite is {convert_to_celsius(f)} celsius .")