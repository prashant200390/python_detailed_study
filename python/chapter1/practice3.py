import os

target_path = "./chapter1"


contents = os.listdir(target_path)


for item in contents:
    print(item)