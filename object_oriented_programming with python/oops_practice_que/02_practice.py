# 2. Write a class “Calculator” capable of finding square, cube and square root of a number.
import math
class calculator: 
    def __init__(self,num):
        self.num = num
    
    def square(self):
        print(f"square of is {self.num**2}.")
    
    def cube(self):
        print(f"cube is {self.num**3}.")
    
    def square_root(self):
        print(f"square root is {math.sqrt(self.num)}.")

c = calculator(9)
c.square()
c.cube()
c.square_root()