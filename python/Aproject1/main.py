import random
computer = random.choice([1, 0, -1])
user_str = input("Enter your move in r as rock , p as paper and s as scissor : ")
dict = {"r" : 1 , "p" : 0 , "s" : -1}
reverse_dict = { 1 : "rock" , 0 : "paper" , -1 : "scissor"}
user = dict[user_str]

print(f"you choose {reverse_dict[user]} and computer choose {reverse_dict[computer]}.")

if (user == computer):
    print("It's a draw.")
else:
    if(computer == 1 and user == 0 ):
        print("You win !")
    elif(computer == 1 and user == -1):
        print("You lose !")
    elif(computer == 0 and user == 1):
        print("You lose !")
    elif(computer ==-1 and user == 1):
        print("You win !")
    else:
        print("Something is wrong on your side.")

