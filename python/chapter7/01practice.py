# 1. Write a program to print multiplication table of a given number using for loop.
number = int(input("Enter the number which you want multiplicaiton of : "))

for i in range (1,11):
    multiplication = number * i 
    print(f"{number} * {i} = {multiplication}")
