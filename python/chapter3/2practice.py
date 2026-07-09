# #Write a program to fill in a letter template given below with name and date.
template = """letter = '''
Dear <|Name|>,
You are selected!
<|Date|>
''' """ 

letter = input("Enter the name of letter :")
name = input("Enter the name of reciever :")
date = input("Enter the date : ")

print(template.replace("'''",letter).replace("Name",name).replace("Date",date)) 

# to use mutiple same string funcion include .function after each closed bracket