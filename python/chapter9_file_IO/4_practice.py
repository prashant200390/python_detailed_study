# 4. A file contains a word “Donkey” multiple times. You need to write a program which
# datas this word with ##### by updating the same file.

data = ""
with open("donkey.txt") as f :
    data = f.read()

with open("donkey.txt","w") as f:
    data = data.replace("donkey","#####")
    f.write(data)
