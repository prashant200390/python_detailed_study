#'''f = open("file.txt","r")
# data = f.read()
# print(data)
# another way without need to explicitly close file .
with open("file.txt") as data:
    print(data.read())