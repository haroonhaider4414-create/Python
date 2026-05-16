import random

#dice rolling
while True:
    # roll 2 dices
    die1= random.randint(1, 6)
    die2= random.randint(1, 6)

    #output of the dices
    print("you rolled", die1, " and ", die2)
    print("\nTotal = ", die1+die2)

    # ask user for the choice 
    choice= input("\nDo you want to roll again?(Y/N): ").lower()

    if choice!= "y":
        print("Thanks for playing.")
        break


