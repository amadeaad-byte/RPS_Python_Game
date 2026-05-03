import random

#Player & Program Choices
player_answer = input("Rock, paper, or scissors?: ").lower()
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
    elif()
    else:
        print("I lost! Good game.")

results(player_answer, prog_answer)

#Okay, I got the game working, now I want to make the program ask to play again.
#If the player picks "Yes", the game will restart. If "No", the game will display a "good game" message then stop.

#Play Again?
y = True
n = False

print("Wanna play again? (y/n)")
play_again = input("Enter 'y' to play again or 'n' to quit: ").lower()
if play_again == 'y':
    while True:
        player_answer = input("Rock, paper, or scissors?: ").lower()
        prog_answer = random.choice(prog_choice)
        print("I choose..." + prog_answer + "!")
        print("Player: " + player_answer + ".") 
        results(player_answer, prog_answer)
        print("Wanna play again? (y/n)")
        play_again = input("Enter 'y' to play again or 'n' to quit: ").lower()
        if play_again == 'n':
            print("Good game! Thanks for playing.")
            break