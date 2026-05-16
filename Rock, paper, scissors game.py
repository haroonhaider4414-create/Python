#2 modes  1st:modes player vs player 2nd:player vs comp
#DAY4
import random


#function to choose the mode
def get_choice(player_name):
    while True:
        try:
            choice= int(input(f"{player_name}, choose (1.Rock 2.Paper 3.Scissors):  "))
            if choice in [1, 2, 3]:
                return choicee
            else:
                print("Invalid choice. Enter a number between 1-3.")
        except ValueError:
            print("Enter a number between 1-3")


#determine winner
def determine_winner(p1, p2):
    if p1==p2:
        return "It's a Tie!!"
    elif (p1==1 and p2==2) or (p1==2 and p2==3) or (p1==3 and p2==1):
        return "Player 1 Wins!!"
    else:
        return "Player 2 Wins!!"


# Play with friend

def play_with_friend():
    print("\n Player vs Player")
    while True:
        p1 = get_choice("Player 1")
        print("\n" * 50)
        p2 = get_choice("Player 2")
        choices = {1: "Rock", 2: "Paper", 3: "Scissors"}
        print(f"Player 1 chose {choices[p1]}")
        print(f"Player 2 chose {choices[p2]}")

        print(determine_winner(p1, p2))
        again = input("Do you want to play again(Yes/No): ").lower()
        if again != "yes":
            break


# player vs computer
def play_w_comp():
    print("\n Player vs Computer")
    while True:
        player = get_choice("you")
        computer = random.randint(1, 3)

        choices={1:"Rock", 2:"Paper", 3:"Scissors"}
        print(f"Uou chose: {choices[player]}")
        print(f"Computer chose: {choices[computer]}")

        if player==computer:
            print("It's a Tie!!")
        elif (player == 1 and computer == 2) or (player == 2 and computer ==3) or (player ==3 and computer ==1):
            print("You Win!!")
        else:
            print("Computer Wins!!")

        again=input("Do you want to play again(Yes/No): ").lower()
        if again!= "yes":
            break


# start here
print("This is a 2 modes game.")
print("Read the instructions carefully!!")
print(""""
instructions:-
- Mode 1: Player vs player - Two people take turns playing
- Mode 2: Player vs Computer - Player play with Computer
- 1: Rock, 2: Paper, 3: Scissors""")

# Get mode from user
while True:
    mode = input("Do you want to:\n 1.Player vs Player.\n 2.Player vs Computer.\n(1 or 2): ")
    if mode=="1":
        play_with_friend()
        break
    elif mode=="2":
        play_w_comp()
        break
    else:
        print("Invalid input. try again")












