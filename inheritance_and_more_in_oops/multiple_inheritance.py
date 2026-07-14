# it is another type of inheritance with multiple base class and a single derive class
# to make it understand more easily , i will use term like father,mother and child for classes
class father:
    father_name = "Krishna"
    def father_info(self):
        print(f"Father's name is {self.father_name}.")

class mother:
    mother_name = "Gita"
    def mother_info(self):
        print(f"Mother's name is {self.mother_name}.")

class child(father,mother):
    child_name = "Prabin"
    def child_info(self):
        print(f"And altogether Father's name is {self.father_name}. \n Mother's name is {self.mother_name}. \n Child's name is {self.child_name}.")
a = father()
b = mother()
c = child()
a.father_info()
b.mother_info()
c.child_info()

#and if we asked father_name from child class we will get that info like -
print(c.father_name,c.mother_name)