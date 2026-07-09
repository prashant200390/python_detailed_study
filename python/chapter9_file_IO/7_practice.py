with open("log.txt","r") as f :
    lines = f.readlines()

lineno = 1
for line in lines:
    if("python" in line):
        print(f"'python' is present in line no {lineno}.")
        break
    lineno += 1 
else:
     print("word 'python' is not present in the file .")