# 2. The game() function in a program lets a user play a game and returns the score as an
# integer. You need to read a file ‘Hi-score.txtʼ which is either blank or contains the previous
# Hi-score. You need to write a program to update the Hi-score whenever the game()
# # function breaks the Hi-score.

import random

def game():
    score = random.randint(1,100)
    with open("high_score.txt") as f:
        hscore = f.read()
        if(hscore != ""):
            hscore = int(hscore)
        else:
            hscore = 0
    
    print(f"Your score is {score}.")
    if(hscore < score):
        with open("high_score.txt","w") as f:
            f.write(str(score))
    else:
        return
    

game()