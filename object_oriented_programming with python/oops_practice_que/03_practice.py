# 3. Create a class with a class attribute a; create an object from it and set ‘aʼ directly using
# # ‘object.a = 0ʼ. Does this change the class attribute?

class value:
    a = 5

val = value()
val.a = 0
print(val.a)
print(value.a)

# no it doesn't changes orginal value of class attribute.