# understanding the tuples 
items = (23,33,45,11,10,"Banana",33.33)
# here we use formatted string literal : f-string to write function inside "" inside print
print(f"Type is {type(items)} \n| and length is {len(items)}\n while items = ", items)

# here are some basic funcitons of Tuple 
print(f"number of Banana : {items.count("Banana")}")
print(f"index of Banana : {items.index("Banana")}") 

# here this is something that is not a function but mimics a function 
print("Banana" in items )

# now these functiion works in all integer containing tuple but not here ,
# 1. print(f"max no : {max(items)} | min no : {min(items)}")
# 2. print(f"sum is {sum(items)}")
# print(f"sorted : {sorted(items)}")