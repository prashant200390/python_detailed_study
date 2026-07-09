# 5. Repeat program 4 for a list of such words to be censored.
word = "donkey"
with open("donkey.txt") as f :
    data = f.read()

with open("donkey.txt","w") as f :
    data  = data.replace(word, "@" * len(word))
    f.write(data)