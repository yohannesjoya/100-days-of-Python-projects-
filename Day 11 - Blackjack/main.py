import random
from ART import logo;
import os
# random card generator
def deal_card():
    ''' this gives random card from deck'''
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)
# score calculator definition 
def calculate_score(cards):
    ''' this calculates score to sum , black jack and corrects ace case'''
    if sum(cards)==21 and len(cards)==2:
        return 0
    if 11 in cards and sum(cards)>21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)
def compare(cs,us):
    if cs==0:
        return "computer win with BLACKJACK"
    elif us==0:
        return "user win with BLACKJACK"
    elif us==cs:
        return "draw"
    elif us>21:
        return "user lose"
    elif cs>21:
        return "user win"
    elif us>cs:
        return "user win"
    else:
        return "user lose"
    
def blackjack():     
    os.system('cls' if os.name == 'nt' else 'clear')
    print(logo)
       
    user_cards = []
    computer_cards = []
    is_game_over =False

    for _ in range(2):
        computer_cards.append(deal_card())
        user_cards.append(deal_card())

    # this lets the user to pick or not
    while not is_game_over:
        user_result=calculate_score(user_cards)
        computer_result=calculate_score(computer_cards)

        print(f"user card {user_cards} and score {user_result}")
        print(f"computer first card {computer_cards[0]}")

        if user_result==0 or computer_result==0 or user_result>21:
            is_game_over=True
        else:
            another_card = input("Type 'y' to add another card, type 'n' to pass ").lower()
            if another_card=="y":
                user_cards.append(deal_card())
            else:
                is_game_over=True

    # this let the computer to draw
    while computer_result!=0 and computer_result<17:
        computer_cards.append(deal_card())
        computer_result=calculate_score(computer_cards) 



    print(f" - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ")
    print(f"your cards were {user_cards} and score {user_result}")
    print(f"computer's final hand was {computer_cards} and score {computer_result}")
    final=compare(us=user_result, cs=computer_result)
    print()
    print()
    print(f'''          {final}''')

    print()
    print()
    restart=input("Do you want to restart the game? Type 'y' or 'n' : ").lower()
    if restart=="y":
        
        blackjack()
    else:
        print("Thanks for your time")
        exit()

blackjack()

