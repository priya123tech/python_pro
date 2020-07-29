from random import randint

t=["Rock","Paper","Scissors"]

player=False
while (player==False):
    computer=t[randint(0,2)]
    player=input("Rock ,Paper,Scissors?")
    if computer==player:
        print("Tie")
    elif player=="Rock":
        if computer=="Paper":
            print("You Lose")
        elif computer =="Scissors":
            print("You win")
    elif player=="Paper":
        if computer=="Rock":
            print("You win")
        elif computer =="Scissors":
            print("You lose")
    elif player=="Scissors":
        if computer=="Rock":
            print("You loose")
        elif computer =="Paper":
            print("You win")
    q=input("Want to continue type Y or N ?")
    if (q=="Y"):
        player=False
    else:
        player=True
        print("Game Over")

        