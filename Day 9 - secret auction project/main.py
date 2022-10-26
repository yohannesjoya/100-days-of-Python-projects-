import os
#HINT: You can call clear() to clear the output in the console.
from art import logo

print(logo)
print("Welcome to the secret auction rogram")
catalog = {}
play = "yes"
while play == "yes":
    name = input("What is your Name?  ")
    bid = float(input("What is your bid? $"))
    catalog[name] = bid
    play = input("Are there any other bidders? Type 'yes' or 'no'. ").lower()
    if play == "yes":
         os.system('cls' if os.name == 'nt' else 'clear')
    else:
        max = -1
        winner = ""
        for key in catalog:
            if catalog[key] > max:
                max = catalog[key]
                winner = key
        print(f"The winner is {winner} with a bid of ${max}")
