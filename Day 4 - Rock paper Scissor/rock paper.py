import random
rock = '''
    _______
---'   ____)
      (_____)
 rock  (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
paper     _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
scissors__________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

u=int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissoers.\n"))
set_ = [rock,paper,scissors]
if u>=0 and u<=2:
  print(set_[u])
  pc_choice=random.choice(set_)
  print("Computer chose:")
  print(pc_choice)
  if set_[u]==pc_choice:
    print("Draw")
  elif set_[u]== rock and pc_choice==scissors:
    print("You win")
  elif pc_choice==rock and set_[u]==scissors:
    print("You lose")
# can also be comp>use lose
# and user>comp win
  elif set_[u]==scissors and pc_choice==paper:
    print("You win")
  elif pc_choice==scissors and set_[u]==paper:
    print("You lose")
  elif set_[u]==paper and pc_choice==rock:
    print("You win")
  elif pc_choice==paper and set_[u]==rock:
    print("You lose")
else:
  print("Invalid Input you loose")
