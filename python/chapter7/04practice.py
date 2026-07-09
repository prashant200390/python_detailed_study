# 4. Write a program to find whether a given number is prime or not.
num = int(input("Enter a number : "))

if((num%2)==0 and num>0):
    print(f"number {num} is not a prime.")
else:
    print(f"numbr {num} is a prime number .")