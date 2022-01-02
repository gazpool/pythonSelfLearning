import random
guesses = 0

print("Welcome to the number guessing game!")
topOfRange = input("Pick a number: ")
if topOfRange.isdigit():
        topOfRange = int(topOfRange)

        if topOfRange <= 0:
            print('Oops, please type a number above 0')
            quit()
else: 
    print('Oops, make sure you type a number next time')

r = random.randint(0,topOfRange)

while True:
    guesses += 1
    userGuess = input(f"Guess a number between 0 and {topOfRange} ")
    if userGuess.isdigit():
        userGuess = int(userGuess)
    else: 
        print('Oops, make sure you type a number next time')
        continue
    
    if userGuess == r: 
        print("Well done, you got it!")
        break
    else:
        if userGuess < r:
            print("Too low")
        if userGuess > r:
            print("Too high")

print("You got it in", guesses, "guesses")

