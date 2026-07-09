# 5. Write a program to find the sum of first n natural numbers using while loop.
n = int(input("Enter the number : "))
for i in range(1,n):
    n = n + i

print("sum of first n natural number is ",n)