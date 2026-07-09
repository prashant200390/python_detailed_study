import os

# this line of code is used to determnine path
directorylist = '/'
 
# this is used to extract and store that data inside the content in list datatype
contents = os.listdir(directorylist)

# and finally this code is used for printing that data into the terminal 
print(contents)

