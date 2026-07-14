# 4. Add a static method in problem 2, to greet the user with hello.
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
    
    @staticmethod
    def greet():
        print("hello")

c = calculator(9)
c.greet()
c.square()
c.cube()
c.square_root()