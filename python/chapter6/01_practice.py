# 1. Write a program to find the greatest of four numbers entered by the user.
a = int(input("Enter first number, a :"))
b = int(input("Enter second number, b :"))
c = int(input("Enter third number, c :"))
d = int(input("Enter fourth number, d :"))

if(a>b and a>c and a>d):
    print("a is greater number.",a)
elif(b>a and b>c and b>d):
    print("b is greater number.",b)
elif(c>a and c>b and c>d):
    print("c is greater number.",c)
elif(d>a and d>b and d>c):
    print("d is greater number.",d)
else:
    ("invalid number.")