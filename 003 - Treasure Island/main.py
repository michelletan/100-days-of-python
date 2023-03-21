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

# https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

# Write your code below this line 👇

choice1 = input(
    "There's a fork in the path ahead, where do you want to go? Type 'left' or 'right'. \n>> ")

if choice1 == "right":
    print("A truck appears out of nowhere and crushes you. Game over...")
    quit()
elif choice1 != "left":
    print("You can only choose left or right. Since you haven't made a choice, a hole opens up below you and you fall in. Game over...")
    quit()

choice2 = input(
    "You walk into a large cave with a sparkling pool of water. Type 'swim' to swim across the pool, or 'wait' to wait for a boat. \n>> ")
if choice2 == "swim":
    print("There was a shark in the water! Game over...")
    quit()
elif choice2 != "wait":
    print("You can only choose swim or wait. Since you chose poorly, a passing crocodile gobbles you up. Game over...")
    quit()

choice3 = input("You wait long enough for a mysterious boat to appear. It carries you to the other side of the pool, where there are three doors - red, yellow and blue. Type 'red', 'yellow', or 'blue' to open one of the doors. \n>> ")

if choice3 == "red":
    print("Flames engulf you in an instant. Game over...")
elif choice3 == "yellow":
    print("You made the right choice. Congratulations, you've won!")
elif choice3 == "blue":
    print("A pack of hungry wolves meets your eyes. Game over...")
else:
    print("Why didn't you follow the instructions? Game over...")
