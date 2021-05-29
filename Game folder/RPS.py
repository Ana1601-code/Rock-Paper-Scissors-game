from random import randint 

 #moves for the player
moves = ["rock","paper","scissor"]

while True:
    computer = moves[randint(0,2)]
    player = input("rock, paper or scissor ? (or end the game)").lower()

    if player == "end the game":
        print("The game has ended !")
        break
    elif player == computer:            #condition 1
        print("Tie!")
    elif player == "rock":              #condition 2
        if computer == "paper":
            print("You lose!")
        else:
            print("You win!")
    elif player == "paper":             #condition 3
        if computer == "scissor":
            print("You lose!")
        else:
            print("You Win!")
    elif player == "scissor":           #condition 4
        if computer == "rock":
            print("You lose!")
        else:
            print("You win!")
# if you type wrong spelling 
    else:                               #condition 5
        print("Check your spelling !!")        
    




