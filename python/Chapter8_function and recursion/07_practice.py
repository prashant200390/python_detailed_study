# write a function to remove a word inside a list and also strip words .
def remove(list,word):
    s = []
    for item in list:
        if not(item==word):
            s.append(item.strip(word))
    return s   
l = ["Prashant","Shuvham","Rohan","an"]
print(remove(l,"an"))