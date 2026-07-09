class employee():
    language = "python"
    salary = 1400000

prashant = employee()
print(prashant.language , prashant.salary)

prabin = employee()
prabin.language = "javascript" # we give instance attribute here on same named variable.
print(prabin.salary , prabin.language)

# the question which will print is that always instance attributes have higher authority .