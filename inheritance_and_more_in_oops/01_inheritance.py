# inheritance is the way of programming in which features of one class can be used by another class.
# there is parent class(i.e which provides info) and child class (i.e that inherits properties)
class emp():    # Base or Parent class
    company_name = "Esewa"
    def info(self):
        print(f"name of the company is {self.company_name}.")

class programmer(emp): # Derived or Child class
    language = "python"
    def info(self,name):
        self.name = name
        print(f"{self.name}'s company is {self.company_name} and language is {self.language}.")

a = emp()
b = programmer()
a.info()
b.info("prashant")
print(a.company_name,b.company_name) # here company_name is attribute of base class but we can stil use it with the help of inheritence.