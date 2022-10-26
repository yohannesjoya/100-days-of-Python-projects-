import os

#Step 5

import random


#TODO-1: - Update the word list to use the 'word_list' from hangman_words.py
import hangman_words
word_list=hangman_words.word_list
#Delete this line: word_list = ["ardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 11

#TODO-3: - Import the logo from hangman_art.py and print it at the start of the game.
import hangman_art
print(hangman_art.logo)
stages=hangman_art.stages

#Testing code
# print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
guesses=[]
display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    os.system('cls' if os.name == 'nt' else 'clear')
    # print(f'Pssst, the solution is {chosen_word}.')

    #TODO-4: - If the user has entered a letter they've already guessed, print the letter and let them know.
    
    guesses.append(guess)
    if guesses.count(guess)>1:
      print("You have already guessed this guess")
      
    print(f"you guesses list {guesses}")

    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter

    #Check if user is wrong.
    if guess not in chosen_word:
        #TODO-5: - If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
        lives -= 1
        print(f'''you guessed {guess}, that's not in the word you lose a life and left with {lives} life''')
        if lives == 0:
            end_of_game = True
            print("-------------------------")
            print("You lose.")
            print("-------------------------")
            gain=len(display)-display.count("_")
            score=gain/len(display)
            print(f"Your score is {score*100} %")

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("-------------------------")
        print("You win.")
        print("-------------------------")
        gain=len(display)-display.count("_")
        score=gain/len(display)
        print(f"Your score is {score*100} %")

    #TODO-2: - Import the stages from hangman_art.py and make this error go away.
    print(stages[lives])
    

print("---------------------------------------------------------")    
print(f'Pssst, the solution is | {chosen_word} |.')
print("---------------------------------------------------------")    