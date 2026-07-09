#write a function to find out greater nbr amoung 3 .
def greater(a,b,c):
    if(a>b and a>c):
        print(f"Greater nbr is {a}")
    elif(b>a and b>c):
        print(f"Greater nbr is {b}")
    elif(c>a and c>b):
        print(f"Greater nbr is {c}")
    else:
        print("please provide valid and differnt nbrs . ")
greater(3,5,1)
greater(2,2,1)