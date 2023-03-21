import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Write your code below this line 👇


def print_image(choice):
    if choice == 0:
        print(rock)
    elif choice == 1:
        print(paper)
    elif choice == 2:
        print(scissors)


print("Play Rock, Paper Scissors!")
choice = int(input("Type 0 for rock, 1 for paper and 2 for scissors. >> "))

if choice < 0 or choice > 2:
    print("Invalid input, game over!")
    quit()
else:
    com_choice = random.randint(0, 2)

    print("You chose: \n")
    print_image(choice)
    print("Computer chose: \n")
    print_image(com_choice)

    if com_choice == choice:
        print("Draw! Try again?")
    elif com_choice - 1 == choice:
        print("You lose. Try again?")
    elif com_choice + 1 == choice:
        print("You win! Congrats!")
