# 3. Write a program to generate multiplication tables from 2 to 20 and write it to the different
# files. Place these files in a folder for a 13-year-old.

def table(n):
     data = ""
     for i in range(1,11):
        ans = n * i
        data += (f"{n} x {i} = {ans}\n")
     with open(f"table/{n}.txt","w") as f:
        f.write(data)

for i in range(2,21):
    table(i)

# program is good to go n0w and it okay as f ;