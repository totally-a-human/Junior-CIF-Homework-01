from random import randint

answer="yes"

range_number = int(input("Enter the upper limit for the random number: "))
random_number = randint(1, range_number)

while answer=="yes":
   
    guess = int(input("Guess a number between 1 and " + str(range_number) + ": "))

    if guess == random_number:
       print("You guessed it!")
       answer="no"
    else:
     if guess < random_number:
         print("Your guess was too low.")
     if guess > random_number:
            print("Your guess was too high.")
     answer=input("would you like to try again?")
     if answer == "no":
         print("Thanks for playing!")