# 2. Write a program to find out whether a student has passed or failed if it requires a total of 40% and at least 33% in each subject to pass. Assume 3 subjects and take marks as an input from the user.
s1 = float(input("Enter the marls of 1st subject :"))
s2 = float(input("Enter the marls of 2nd subject :"))
s3 = float(input("Enter the marls of 3rd subject :"))
total = 75
p1 = (s1/total)*100
p2 = (s2/total)*100
p3 = (s3/total)*100

totalpercent = (s1+s2+s3)/(total*3)*100

if(p1>33 and p2>33 and p3>33 and totalpercent>40):
    print("student is passed with total of",totalpercent,"%")
else:
    print("student is failed due to",totalpercent,"%")