# 9. Write a program to find out whether a file is identical and matches the content of another
#    file.
with open("file.txt") as f:
    data1 = f.read()

with open("copy_file.txt") as f:
    data2 = f.read()

if(data1.lower() == data2.lower()):
    print("content is same in both files.")
else:
    print("content is differnt in both files.")