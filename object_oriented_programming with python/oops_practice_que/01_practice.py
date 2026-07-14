# 1. Create a class “Programmer” for storing information of few programmers working at Microsoft.
class programmer:
    company = "Microsoft"
    def __init__(self,name,language,post,salary,contact):
        self.name = name 
        self.language = language
        self.post = post
        self.salary = salary
        self.contact = contact
        print(f"name is {self.name} \n language is {self.language}\n post is {self.post} \n salary is {self.salary}\n and finally contact info is {self.contact}")

name = input("enter the name of employee : ")
language = input("enter programming language he use : ")
post = input("enter the post of the person in company : ")
salary = input("enter the salary of this person : ")
contact = input("enter the contact information of this person : ")

programmer(name,language,post,salary,contact)
# just to understand easily what's going on i asked user for the details instead of simply giving inside ()