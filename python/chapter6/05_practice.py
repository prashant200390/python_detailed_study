# 5. Write a program which finds out whether a given name is present in a list or not.
list = ["prashant","samriddhi","queen","raju"]
name = input("Enter your name : ")

if(name in list):
    print(name," is in the list.")
else:
    print(name," is not in the list")