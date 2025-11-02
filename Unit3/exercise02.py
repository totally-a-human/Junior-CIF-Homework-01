from random import randint

number=3

range_number = int(input("Enter the upper limit for the random number: "))
random_number = randint(1, range_number)

while number>0:
   
    guess = int(input("Guess a number between 1 and " + str(range_number) + ": "))

    if guess == random_number:
       print("You guessed it!")
       number=-1
    else:
     if guess < random_number:
         print("Your guess was too low.")
     if guess > random_number:
            print("Your guess was too high.")
     answer=input("Would you like to try again? You have " + str(number) + " attempts left.")
     if answer == "yes":
         number=number-1
     if answer == "no":
         number=-1
         print("the random number was " + str(random_number))
if number==0:
    print("You've used all your attempts. The number was " + str(random_number))
print("Thanks for playing!")