# guessing a number game
from random import randint
score = 0

print("Welcome to my random game")
name = input("What is your name?  ")
print(f"Welcome {name}, You have 10 attempts to guess a random number between 1 and 10")

for i in range(10):
    randomNum = randint(1, 10)
    guess = int(input("guess the random number: "))
    if guess == randomNum:
        score = score + 5
        print("Bravo you have 5 points in the bag!")
    else:
        print(f'oops! you got that wrong! the correct answer is not {guess} it is {randomNum}')
        print(f"try again you have {10 - (i+1)} more attempts")

print("game over!")
print(f"You have a total of {score} points")



