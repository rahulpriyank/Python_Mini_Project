from asyncore import write
import random

print("Welcome To the Guess Game of Rahul CodeWorld")
randNumber = random.randint(1,100)
userGuess = None
Guess = 0

while (userGuess != randNumber):

    userGuess = int(input("Enter Your Guess : "))
    Guess += 1  
    if (userGuess == randNumber):
        print("You Guessed it Correct")

    else:
        if(userGuess>randNumber):
            print("Guess a Smaller Number")
        else:
            print("Guess a Greater Number")
      
print(f"You Guessed the Number in {Guess} Guesses")
print("You Just Broke the Highscore")
with open("Highscore.txt", "r") as f :
    Highscore = int(f.read())

if(Guess<Highscore): 
    with open("Highscore.txt", "w") as f :
        f.write(str(Guess))