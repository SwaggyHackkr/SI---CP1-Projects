#SI, Period 1, Dice roller assignment 

import random

# Ask the user which dice they want to roll
choice = input("Which dice would you like to roll? (D4, D6, D8, D10, D12, D20): ")

# Figure out the dice size based on their choice 

if choice == "D4":
    roll = random.randomint(1, 4)
elif choice == "D6":
    roll = random.randint(1, 6)
elif choice == "D8":
    roll = random.randint(1, 8)
elif choice == "D10":
    roll = random.randint(1, 10)
elif choice == "D12":
    roll = random.randint(1, 12)
elif choice == "D20":
    roll = random.randint(1, 20)
else:
    roll = None
    print("That's not a valid dice size!")


# Tell the use what they rolled 
if roll is not None:
    print("You rolled a " + str(roll) + "!")