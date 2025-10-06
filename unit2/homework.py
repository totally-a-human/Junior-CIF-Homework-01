from random import randint

random_number = randint(1, 100)
guess = int(input("Guess a number between 1 and 100"))

if guess == random_number:
    print("You guessed it!")
else:
    print("Wrong, the number was " + str(random_number))