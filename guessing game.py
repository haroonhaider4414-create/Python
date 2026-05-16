import random

secret_number = random.randint(1, 100)
print("Welcome to the Guess the number game!")
print("I have selected a number between 1 and 100")
while True:
    guess= int(input("Enter the your guess: "))
    if guess < secret_number:
        print("Too low! Try again")
    elif guess > secret_number:
        print("Too high! Try again")
    else:
        print("You have guessed it correctly")
        break









