import random
import os
# logo
from art import logo
from art import vs
print(logo)
# game data
from data import data

def HLgame(a,score):
    print(f"your current score is {score}")
    print(f"Compare A: {a['name']}, a {a['description']}, from {a['country']}")
    print(vs)
    b=random.choice(data)
    print(f"Against B: {b['name']}, a {b['description']}, from {b['country']}")
    ans=input(f"Who has more followers? Type 'A' or 'B' :")
    if a['follower_count']>b['follower_count']:
        result = "A"
        correct = a
    elif a['follower_count']<b['follower_count']:
        result = "B"
        correct = b
    else:
        print("they have equal followers")
    if ans!=result:
        print(f"your score is {score}")
        print(f"    -        Compare A: {a['name']}, a {a['description']}, from {a['country']} with {a['follower_count']} FOLLOWERS")
        print(f"    -        Compare B: {b['name']}, a {b['description']}, from {b['country']} with {b['follower_count']} FOLLOWERS")

        print("GAME ENDED")
    else:
        score+=1
        print(f"your current score is {score}")
        os.system('cls' if os.name == 'nt' else 'clear')
        HLgame(correct, score)
a = random.choice(data)  # this is the starting person
HLgame(a, 0)