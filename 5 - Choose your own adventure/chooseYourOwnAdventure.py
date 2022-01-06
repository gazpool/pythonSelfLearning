userName = input("Welcome adventurer, what is your name? ")

answer = input(f"Well, {userName}, are you ready to embark on your journey? (yes/no) ")

if answer == "no":
    print("OK, maybe next time")
elif answer == "yes":
    answer = input("You are walking along a dirt path and come to a fork in the road, which way do you wish to go? (left/right)? ")

if answer == "left":
    answer = input("You come accross a fast flowing river, do you want to try swim accross or walk around until you find a crossing (swim/walk)? ")
    if answer == "swim":
        print("You try to swim across but the current is too strong, you are sucked under the water and drown.")
        print("GAME OVER")
    elif answer == "walk":
        print("You walk for miles without finiding a crossing, you realise you forgot to bring any water and do not have the energy to make it back.")
        print("GAME OVER")
    else:
        print("You failed to choose a valid option")
        print("GAME OVER")
if answer == "right":
    answer = input("After walking for a while you come across a beggar on the road, they ask you for a coin. What do you wish to do (give/ignore)? ")
    if answer == "ignore":
        print("You flip the beggar off and tell him to get a real job, as you turn your back to walk away they slit your throat.")
        print("GAME OVER")
    elif answer == "give":    
        print("After recieving the coin the beggar lowers their hood and reveals they are actually the king, they reward your generosity by making you a knight")
        print("YOU WON!")
    else:
        print("You failed to choose a valid option")
        print("GAME OVER")
