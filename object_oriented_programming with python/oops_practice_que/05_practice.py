# 5. Write a Class ‘Trainʼ which has methods to book a ticket, get status (no of seats) and get
# fare information of train running under Indian Railways.
from random import randint
class train : 
    railways = "Indian Railways"
    def __init__(self,train_no):
        self.t = train_no
        self.av_seat = randint(2000,2600)
        self.fare = {
            "delhi" : 2500,
            "rajistan" : 3600,
            "kerala" : 3400
        }
    
    def getstatus(self):
        print(f"Available seat is {self.av_seat}")

    def fareinfo(self,destination):
        self.d = destination
        if self.d in self.fare:
            print(f"fare is {self.fare[self.d]} for {self.d}.")
        else:
            print("Tain for this destination is not currently available.")

prashant = train("2A")
prashant.getstatus()
prashant.fareinfo("kerala")