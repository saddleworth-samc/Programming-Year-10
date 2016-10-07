# Import Libraries
import random

# Set flag variables
runAgain = 'y'
score = 0

#Loop until the user wants the program to end
while runAgain == "y":
    #Initialise the cups and randomly place the ball
    cups = [0, 0, 0]
    ballPosition = random.randrange(0, 2)
    cups[ballPosition] = 1

    #Display the welcome screen and
    strScore = str(score)
    print("Guess where the ball is!")
    print("You score: " + strScore)

    #Get the cup choice from the user
    guess = input("Which cup is the ball in, cup A, B, or C?")

    # Convert it to uppercase to make a validation eaisier
    guess = guess.upper()

    # Chuck which cup they chose and convert this to the corresponding
    # position in our list. Use -1 for an invalid choice
    if guess == 'A':
        guessPos = 0
    elif guess == 'B':
        guessPos = 1
    elif guess == 'C':
        guessPos = 2
    else:
        guessPos = -1
    # Check whether the ball is in that position
    if guessPos != -1:
        if cups[guessPos] == 1:
            # If so, increment the score and say well done
            print("Well Done! The was in Cup " + guess)
            score = score + 1
        else:
            # If not, inform the user
            print("Bad luck. The ball wasn't in Cup " + guess)
    else:
            #If they didn't type  A, B, or C, tell them!
            print("Invalid choice! Please pick A.B or C next time!")

    # Ask the user if they wish to run the program again
    runAgain = input("Press y to go again.")

    #Display their final score on exit
strScore = str(score)
print("Final Score: " + strScore)
input("Press enter to exit")