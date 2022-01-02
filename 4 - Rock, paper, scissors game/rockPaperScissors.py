import random

userWins = 0
computerWins = 0
draws = 0

options = ["rock","paper","scissors"]


while True:
    userInput = input("Type Rock, Paper, Scissors (or Q to end) ").lower()  
    if userInput == 'q':
        break

    if userInput not in ["rock","paper","scissors"]:
        continue

    rNumber = random.randint(0,2)
# 0 = rock, 1 = paper, 2 = scissors
    computerGuess = options[rNumber]
    print(f"You picked {userInput}, the computer picked {computerGuess}...")

    if userInput == "rock" and computerGuess == "scissors":
        print("You won!")   
        userWins += 1
        
    elif userInput == "paper" and computerGuess == "rock":
        print("You won!")   
        userWins += 1
        
    elif userInput == "scissors" and computerGuess == "paper":
        print("You won!")   
        userWins += 1
    elif userInput == computerGuess:
            print("You and the computer picked the same, it's a draw")
            draws += 1
    else:
        print("Computer wins!")
        computerWins += 1

print("You won",userWins,"times, computer won", computerWins, "times,",draws,"draws")
if userWins < computerWins:
    print("Computer wins, better luck next time")
elif userWins > computerWins:
    print("Well done, you beat the computer!")
else:
    print("It's a draw!")