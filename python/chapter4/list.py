# learning lists right now in python 
friends = ["apple","raju","biswanath",33.33, 23,44.22345,False,True]
print(f"Type : {type(friends[0])} | Value : {friends[0]}")
print(f"Type : {type(friends[1])} | Value : {friends[1]}")
print(f"Type : {type(friends[2])} | Value : {friends[2]}")
friends[0] = "Banana" # lists are mutable , can change value of any index 
print(friends[0]) 