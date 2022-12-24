#ROCK PAPER SCISSOR GAME
import random
player_input=input("Enter the choice: rock, paper, scissor ")
possible_action = ["rock", "paper","scissor"]
computer_input = random.choice(possible_action)
print("Your input is: ",player_input)
print("computer input is: ",computer_input)
if player_input==computer_input:
    print("Draw")
elif player_input =="rock" and computer_input=="paper":
    print("computer win")
elif player_input=="scissor" and computer_input=="rock":
    print("computer is win")
elif player_input=="paper" and computer_input=="scissor":
    print("computer is win")
elif player_input=="paper" and computer_input=="rock":
    print("player is win") 
elif player_input=="rock" and computer_input=="paper":
    print("player is win")
elif player_input=="scissor" and computer_input=="paper":
    print("player is win")

                   

