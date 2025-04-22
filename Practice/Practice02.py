
#Number Guessing Projcet


#for random module
import random
number=random.randrange(1,1000)

#user INPUT 
userInput = int(input("Enter Your Guessed Number Below 1000 :   "))


if userInput>number:
    #If number is TOO HIGH
    print("Computer Guess Number",number)
    print("You guess Too high Number")
    print("Try Again!")

elif number>userInput:
    #If number is TOO LOW
    print("Computer Guess Number: ",number)
    print("You guess Too low Number")
    print("Try Again!")
else:
    #If number is EQUAL 
    print("Computer Guess Number: ", number)
    print("You guess number as Equal to Computer Guess.")