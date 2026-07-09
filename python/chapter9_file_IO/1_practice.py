# 1. Write a program to read the text from a given file ‘poems.txtʼ and find out whether it contains the word ‘twinkleʼ.
with open("poem.txt") as p:
    content = p.read().lower()
    if "twinkle" in content :
            response = "yes , it  definitely contails 'twinkle' in it. "
            print(response)
    else:
            print("No , it doesn't contains 'twinkle' in it .")