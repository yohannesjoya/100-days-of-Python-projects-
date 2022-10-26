print('''
*******************************************************************************
                                        _                 
                                       | |                
              __ _  __ _ _ __ ___   ___| |__   ___  _   _ 
             / _` |/ _` | '_ ` _ \ / _ \ '_ \ / _ \| | | |
            | (_| | (_| | | | | | |  __/ |_) | (_) | |_| |
             \__, |\__,_|_| |_| |_|\___|_.__/ \___/ \__, |
              __/ |                                  __/ |
              |___/                                  |___/ 


*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇
L_R=input('''You're at a cross road. Where do you want to go? Type "left"or "right"\n  ''').lower()
if L_R=="left":
  Wait_Swim = input('''You come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across\n  ''').lower()
  if Wait_Swim=="wait":
    color=input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. which color do you choose?\n  ").lower()
    
    if color=="yellow":
      print("Congrats!! You Win")
    elif color=="blue" or color=="red":
      print("You enter a room of beasts. Game over")
    else:
      print("X X Invalid input for color X X")
  elif Wait_Swim=="swim":
    print("Game over. You choose to swim and got harmed by SHARKS ")
    
  else:
    print("Invalid input to travel across the Sea")
elif L_R=="right":
  print("Game Over. you turn right and fall to hole")
else:
  print("X X Invalid input for direction X X")
    
