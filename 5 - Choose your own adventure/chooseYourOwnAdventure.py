userName = input("Welcome adventurer, what is your name? ")
print(userName)
answer = input(f"Well, {userName}, are you ready to embark on your journey? (yes/no) ")

if answer.lower == "no":
    print("OK, maybe next time")
elif answer.lower == "yes":
    answer = input("You are walking along a dirt path and come to a fork in the road, which way do you go? (left/right)? ")

if answer.lower == "left":
    answer = input("You come accross a fast flowing river, do you want to try swim accross or walk around until you find a crossing (swim/ walk)? ")
    if answer.lower == "swim":
        print("You try to swim across but the current is too strong, you are sucked under the water and drown")
        print("GAME OVER")
    elif answer.lower == "walk":
        print("You walk for miles without finiding a crossing, you realise you forgot to bring any water and do not have the energy to make it back")
        print("GAME OVER")
    else:
        print("You failed to choose a valid option")
        print("GAME OVER")