# 8. Write a program to make a copy of a text file “this.txt”.
with open("file.txt") as f :
    data = f.read()

with open("copy_file.txt","w") as f :
    f.write(data)
