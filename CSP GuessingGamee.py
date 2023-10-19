# things that belong at the top

import random

import time

secret = random.randint(1,100)

guesses = 0
count = 0

# blah blah talking stuff

playing = input("Would you like to play magic number? Y/N ")

# let the games begin

if playing == "Y":
    print("Welcome to magic number!")
    time.sleep(1.8)
    print("The rules are simple.")
    time.sleep(1.5)
    print("I have a number between 1 and 100 and you have to guess what it is.")
    time.sleep(2.5)
    print("There are 3 options for difficulty, Easy, Medium, Hard.")
    difficulty = input("Which difficulty would you like? ")
    if difficulty == "Easy":
        print("Easy difficulty selected!")
        guesses = 9
    elif difficulty == "Medium":
        print("Medium difficulty selected!")
        guesses = 6
    elif difficulty == "Hard":
        print("Hard difficulty selected!")
        guesses = 3
    elif difficulty == "sus":
        print("Cheat Code Activated!")
        guesses = 100000
    
    while True:
        guess = input("Guess a number between 1 and 100: ")
        count = count + 1
        if int(guess) == int(secret):
            print("Correct! you got it in " + str(count) + " Attempts!")
            break
        elif count == guesses:
            print("All out of attempts! The number was " + str(secret))
            break
        elif int(guess) < int(secret):
            print("Higher")
        elif int(guess) > int(secret):
            print("Lower")

# player upsets the game
elif playing == "N":
    print("I guess you just hate fun.")
    time.sleep(2.5)
    print("The game isnt that cool anyways...")
    time.sleep(4)
    print("Im not sad.")
    time.sleep(2.5)
    print("Just dissapointed.")
    time.sleep(5)
    print("please play the game")