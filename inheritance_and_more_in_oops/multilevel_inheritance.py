# there are basically 3 types of inheritence (fyi single, multiple and multilevel)
# now its multilevel inheritance 
# to simply put it in pieces , it is layered inheritence like grandpa to father and father to son.
class grandfather:
    grandpa_name = "Tek Narayan"

class grandmother:
    grandma_name = "Khuma Kala"

class father(grandfather,grandmother): # first inheritance
    father_name = "Maniram"
    def father_info(self):
        print(f"Father's father is {self.grandpa_name} and mother is {self.grandma_name}.")

class mother:
    mother_name = "Isori"

class son(father,mother): # second inheritance
    son_name = "Ramu"
    def son_info(self):
        print(f"And altogether Father's name is {self.father_name}. \n Mother's name is {self.mother_name}. \n Child's name is {self.child_name}.")
class grandson(son):
    grandson_name = "Rahul"
    def grandson_info(self):
        print(f"aafno naam : {self.grandson_name} \n Ba ko naam : {self.son_name}\n Hajurama ko naam : {self.mother_name}\n Jijuba is {self.grandpa_name} \n and Jijuama is {self.grandma_name}. ")
g = grandson()
g.grandson_info()

# and we can get all the heirachy info by simply accessing grandson.
print(g.son_name ,g.father_name, g.mother_name, g.grandma_name , g.grandpa_name , g.grandson_name)