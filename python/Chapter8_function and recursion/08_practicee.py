# 8. Write a python function to print multiplication table of a given number.
def multiply(n):
    for i in range(1,11):
        m = i * n
        print(f"{n} X {i} = {m}")
number = int(input("Enter the value of n : "))
multiply(number)