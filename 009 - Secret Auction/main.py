# from replit import clear
import os
import art


def sys_clear():
    os.system("clear")


print(art.logo)
print("Welcome to the secret auction program \n")

# Get user input for bidders
bidders = []
count = 1
done = False
while not done:
    name = input(f"Bidder #{count}, what is your name? \n >> ")
    bid = float(input("What is your bid? \n >> $"))
    user_done = input(
        "Are there any other bidders? Type 'yes' or 'no'. \n >> ")

    bidders.append({"name": name, "bid": bid})

    if user_done == "no":
        done = True

    count += 1
    sys_clear()

# Calculate the winner of the auction
winner = max(bidders, key=lambda k: k["bid"])
win_bid = "{:.2f}".format(winner["bid"])
print(art.logo)
print(f"The winner is {winner['name']}, with a wnining bid of ${win_bid}!")
