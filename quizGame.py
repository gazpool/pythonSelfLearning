print("Welcome to my animal quiz")
play = input("Do you want to play? ")
if play.lower() != "yes":
	print("Okay, maybe another time")
	quit() 

print("okay letsss go!")
score = 0

answer = input("What is the fastest animal on land? ")
if answer.lower() == "cheetah":
	print("Correct, well done!")
	score += 1
else: print("Incorrect, better luck next time")



