# this the efficient and clean way for the previous problem.
f = open("madara.txt")
p = f.readline()
while(p != ""):
    print(p,type(p))
    p = f.readline()
f.close()