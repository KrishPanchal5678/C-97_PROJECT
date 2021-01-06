import random

print("Guess The Number!")
print("You have 5 chances")

number = random.randint(1, 15)

chances = 0

print("Guess a number between 1 - 15")

while chances < 5:

    Guess = int(input("Enter your Guess: "))

    if (Guess == number):
        print("Congratulations! You guessed the number!")
        break

    elif (Guess < number):
        print("You guessed too low! Try to guess a number higher than " , Guess)

    else: 
     print("You guessed too high! Try to guess a number smaller than " , Guess)
     
    chances += 1
    
    if (Guess != number):
        print("You lost one chance!")

if not chances < 5:
    print("You lost! Better Luck Next Time.. ")
    print("The number was " , number)
