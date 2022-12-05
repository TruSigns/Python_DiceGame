import random

# Randomly roll the dice

again = True


while again:
    #randomly print a number from 1-6
    print(random.randint(1,6))

    #ask user do they want to roll again?
    another_roll = input("Do you want to roll again?(y/n) \n ")


    if another_roll.lower() == "y":
        continue
    else:
        break





