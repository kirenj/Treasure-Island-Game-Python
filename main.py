print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

direction_choice = input("You are at a cross road. Where do you want to go? Type 'left' or 'right': ").lower()
if direction_choice == 'right':
  swim_or_wait = input("You need to reach the treasure island. Do you want to swim to it or wait for a boat? Type 'swim' or 'wait': ").lower()
  if swim_or_wait == 'wait':
    door_selection = input("Great! You safely reached the Island. As the final step, you are greated with 3 doors, which one do you choose. Type 'red', 'blue', or 'green': ").lower()
    if door_selection == 'blue':
      print("You chose the right door. You Win the Treasure!!")
    elif door_selection == 'red' or door_selection == 'yellow':
      print("Oops!!! there is nothing behind your chosen door. Game Over!!!")
      exit()
    else:
      print("You didn't type the correct choice!! Game over!")
      exit()
  elif swim_or_wait == 'swim':
    print("You got attacked by a shark! Game Over!!")
    exit()
  else:
    print("You didn't type the correct choice!! Game over!")
    exit()
elif direction_choice == 'left':
  print("You fell into a hole! Game Over!")
  exit()
else:
  print("You didn't type the correct choice!! Game over!")
  exit()
