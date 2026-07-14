# # 6. Can you change the harry-parameter inside a class to something else (say “harry”)? Try
# changing harry to “slf” or “harry” and see the effects.
from random import randint
class train : 
    railways = "Indian Railways"
    def __init__(harry,train_no):
        harry.t = train_no
        harry.av_seat = randint(2000,2600)
        harry.fare = {
            "delhi" : 2500,
            "rajistan" : 3600,
            "kerala" : 3400
        }
    
    def getstatus(harry):
        print(f"Available seat is {harry.av_seat}")

    def fareinfo(harry,destination):
        harry.d = destination
        if harry.d in harry.fare:
            print(f"fare is {harry.fare[harry.d]} for {harry.d}.")
        else:
            print("Tain for this destination is not currently available.")

prashant = train("2A")
prashant.getstatus()
prashant.fareinfo("kerala")

# so technically , here it does it's job as usuall even if we change (self) to (harry) or (anthing)