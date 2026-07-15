class delhi ():
    def __init__(self):
        print("this is from delhi !")
    
    @staticmethod
    def population():
        print("population is huge by the way !")

class mumbai(delhi):
    def __init__(self):
        print("this is from mumbai !")
        super().__init__()
        super().population()
        
class rajistan(mumbai):
    def __init__(self):
        print("this is from rajistan !")
        super().__init__()

location2 = rajistan()
# fyi super() keyword helps to execute function of parent class.
''' 
output :

this is from rajistan !
this is from mumbai !
this is from delhi !
population is huge by the way ! '''
