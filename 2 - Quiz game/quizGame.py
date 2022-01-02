print("Welcome to my animal quiz")

play = input("Do you want to play? ")

if play.lower() != "yes":
	print("Okay, another time then...")
	quit() 

print("okay letsss go!")
score = 0
qCount = 0

answer = input("What is the fastest animal on land? ")
if answer.lower() == "cheetah":
	print("Correct, well done!")
	score += 1
else: print("Incorrect, better luck next time")
qCount += 1

answer = input("What colour is an orangutan? ")
if answer.lower() == "orange":
	print("Correct, well done!")
	score += 1
else: print("Incorrect, better luck next time")
qCount += 1

answer = input("How many tentacles does an octopus have? ")
if answer.lower() == "eight" or answer == "8": 
	print("Correct, well done!")
	score += 1
else: print("Incorrect, better luck next time")
qCount += 1

answer = input("What is a rhino's horn made of? ")
if answer.lower() == "keratin": 
	print("Correct, well done!")
	score += 1
else: print("Incorrect, better luck next time")
qCount += 1

answer = input("Where country do Panda's come from? ")
if answer.lower() == "china": 
	print("Correct, well done!")
	score += 1
else: print("Incorrect, better luck next time")
qCount += 1


perc = round(score/qCount*100,2)



if qCount == score:
		print("Congratulations! You got all the questions correct, give yourself a pat on the back")
elif score == 0:
		print("Epic fail!! You got 0 questions correct, go study some more")
else: print (f"Good effort. You got {score} out of {qCount} questions correct ({perc}%)")
