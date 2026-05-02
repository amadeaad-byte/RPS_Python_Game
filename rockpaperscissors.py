import random

#Player & Program Choices
player_answer = input().lower()
prog_choice = ["rock","paper","scissors"]
prog_answer = random.choice(prog_choice)

#Displaying program choice
print("I choose..." + prog_answer + "!")
print("Player: " + player_answer + ".") 

#Determining Results
def results(player, program):
    if player == program:
        print("Dang! We Tied! Let's try again.")
    elif( 
        (program == "rock" and player == "scissors") or
        (program == "paper" and player == "rock") or
        (program == "scissors" and player == "paper")
    ):
        print("I win! Good game.")
    else:
        print("I lost! Good game.")

results(player_answer, prog_answer)