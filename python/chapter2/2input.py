# this is the example to corner the input() function problem while adding 
a = input("Enter the 1st number : ")
b = input("Enter the 2nd number : ")

print("first number is ",a)
print("second number is ",b)
print("sum of a and b : ", a+b)
# this gives 22 in ans because it adds two strings not integers

# this one is the correct way to display and sum two numbers while usng input() funciton
a = int(input("Enter the 1st number : "))
b = int(input("Enter the 2nd number : "))

print("the sum of a and b : ", a+b)