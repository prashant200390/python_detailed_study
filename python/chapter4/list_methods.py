list = [ 23 , 33 , 54 , 11 , 20 , 10 ]

print("initial :",list)

list.sort() # it sorts the data inside the list in ascending order 
print("sorting : " ,list)

list.reverse() # it reverse the data form backward as it is 
print("reverse :",list)

list.append(82) # it adds a new data after last index 
print("append",list)

li = list.pop(6)  # it delets the data in certain index but also can return the removed vlaue 
print("pop : ",list)
print("poped value :" , li)

list.insert(3,34) # it inserts data in certain index without deleting orignal one by just shifting orignal in next index 
print("insert : ",list)

list.remove(20)  # unlike .pop function , it removes by value instead of index and doesn't returns the deleted value 
print("remove : ", list)