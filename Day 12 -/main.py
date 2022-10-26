import os
import random
guesslist=[]
for i in range(1,101):
    guesslist.append(i)
         
def guessGame():    
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    level=input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    rand = random.choice(guesslist)
    if level=="easy":
        life=10
    elif level=="hard":
        life=5
    else:
        print("Invalid input of Level")
        exit()
        
    while life>0:

        print(f"You have {life} attempts remaining to guess the number.")
        guessed=int(input("Make Guess: "))
        
        if guessed==rand:
            print()
            print("Well Done You have managed to Win")
            print()
            again=input("Do you Want to play Again? Type 'y' or 'n': ")
            if again=='y':
                os.system('cls' if os.name == 'nt' else 'clear')
                guessGame()
            else:
                print()
                print("Thanks for your time")
                print()
                exit()
        elif guessed<rand:
            print("Too Low.")
        else:
            print("Too High")
            

        life -=1
    
    again=input("Do you Want to play Again? Type 'y' or 'n': ")
    if again=='y':
        os.system('cls' if os.name == 'nt' else 'clear')
        guessGame()
    else:
        print()
        print("Thanks for your time")
        print()
        exit()

guessGame()     
