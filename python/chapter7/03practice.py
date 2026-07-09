# 3. Attempt problem 1 using while loop.
number = int(input("Enter the number for the multiplication table : "))
i = 1 
while(i<=10):
    multiply = number * i 
    print(f"{number} * {i} = {multiply}")
    i += 1