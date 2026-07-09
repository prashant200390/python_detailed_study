class emp :
    language = "python"
    salary = 1400000
    @staticmethod
    def greet():
        print("HELLO MAN !")

prashant = emp()
print(prashant.language , prashant.salary)
prashant.greet()