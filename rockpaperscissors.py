import random

#Player & Program Answers
player_answer = input("Rock, paper, or scissors?: ").lower()
prog_choice = ["rock","paper","scissors"]
prog_answer = random.choice(prog_choice)

#Displaying program choice
print("I choose..." + prog_answer + "!")
print("Player: " + player_answer + ".") 

#Determining Results
def results(player, program):
    while True:
        if player == program:
            print("Dang! We Tied! Let's try again.")
        elif( 
            (program == "rock" and player == "scissors") or
            (program == "paper" and player == "rock") or
            (program == "scissors" and player == "paper")
        ):
            print("I win! Good game.")
        elif(
            (player == "rock" and program == "scissors") or
            (player == "paper" and program == "rock") or
            (player == "scissors" and program == "paper")
        ):
            print("I lost! Good game.")
        else:
            print("Invalid input. Please choose rock, paper, or scissors.")
        return
results(player_answer, prog_answer)


#Play Again Loop
# Problem: This part works, but there is a problem with the loop. The "good game, thanks for playing." message doesn't print after the user 
# inputs "no" after the first game. It only prints after the user inputs "no" after the second game. I think this is because the 
# loop is set to continue until the user inputs "no", but it doesn't check for that condition until after the first game is played. 
# To fix this, I can add a check for the "no" input before the loop starts, and if the user inputs "no", it will print the 
# message and exit the program immediately. 

yes = True
no = False

print("Wanna play again? (yes/no)")
play_again = input("Enter 'yes' to play again or 'no' to quit: ").lower()
if play_again == 'yes':
    while True:
        player_answer = input("Rock, paper, or scissors?: ").lower()
        prog_answer = random.choice(prog_choice)
        print("I choose..." + prog_answer + "!")
        print("Player: " + player_answer + ".") 
        results(player_answer, prog_answer)
        print("Wanna play again? (yes/no)")
        play_again = input("Enter 'yes' to play again or 'no' to quit: ").lower()
        if play_again == 'no':
            print("Good game! Thanks for playing.")
            break
        else: 
            print("Invalid input. Please enter 'yes' or 'no'.")
            continue