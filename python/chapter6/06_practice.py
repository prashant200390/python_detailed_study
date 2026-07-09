# 6. Write a program to calculate the grade of a student from his marks from the following
# scheme:
# 90 – 100 = Ex
# 80 – 90 = A
# 70 – 80 = B
# 60 – 70 = C
# 50 – 60 = D
# <50 = F
marks1 = float(input("Enter the marks of 1st student : "))
if(marks1>=90 and marks1<=100):
    print("Excellent :  with marks of ",marks1)
elif(marks1>=80 and marks1<90):
    print("A with marks of ",marks1)
elif(marks1>=70 and marks1<80):
    print("B with marks of ",marks1)
elif(marks1>=60 and marks1<70):
    print("C with marks of ",marks1)
elif(marks1>=50 and marks1<60):
    print("D with marks of ",marks1)
elif(marks1<50 and marks1>=0):
    print("F with marks of ",marks1)
elif(marks1<0):
    print("invalid marks!")