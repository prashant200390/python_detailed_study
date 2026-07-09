# 6. Write a program to mine a log file and find out whether it contains ‘pythonʼ.
with open("log.txt") as f :
    data = f.read()

    if("python" in data):
        print("Yes , it contains the word 'python' in log.txt.")
    else:
        print("NO , it doesn't contains the word 'python' in log.txt.")