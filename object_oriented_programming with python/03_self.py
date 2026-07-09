class employee():
    language = "python"
    salary = 1400000
    
    def getinfo(self):
     print(f"language is {self.language} and salary is {self.salary}")

prashant = employee()
prashant.getinfo()
# employee.getinfo(prashant)