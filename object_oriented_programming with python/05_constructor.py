class employee():
    language = "python"
    salary = 1500000
    
    # the __init__ function is a dunden method means it is called automatically and also we can 
    # provide values from outside of the class by adding arguments in this funciton . and 
    # declaring (fyi self.value = vlaue)
    def __init__(self,name,language,salary):
        self.name = name
        self.language = language
        self.salary = salary
        print(f"{self.name}'s language is {self.language} and salary is {self.salary}.")
    
    @staticmethod
    def getinfo():
        print("Hello ! , how are you ?")

prashant = employee("Prashant","javascript",1600000)

prashant.getinfo()