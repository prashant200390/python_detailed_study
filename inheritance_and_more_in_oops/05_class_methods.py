#        Normally we do this,

# class value:
#     a = 22
#     def a_value(self):
#         print(f"value of a is {self.a}")
# given = value()
# given.a = 45
# given.a_value()
# output = value of a is 45

#  but what if we want to print value inside class even if we pass instance attribute 
# for that problem , @classmethod comes in handy
class value:
    a = 22
    @classmethod       # we use this when we need class attribute value
    def a_value(cls):       # we can use anything in place of cls
         print(f"value of a is {cls.a}")

given = value()
given.a = 45
given.a_value()
# output = value of a is 22