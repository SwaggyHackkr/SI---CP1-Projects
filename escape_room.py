# SI, Period 1, Escape Room Assignment

# Escape Room Game
# You have to enter the right code to get out

code = "42"   # the right code

# the clues, they get more obvious each time
clues = [
    "Hint: a famous baseball player uses this number",
    "Hint: its a pronic number",
    "Hint: its 6 times 7",
    "Hint: its the number after 41"
]

print("You are locked in a room.")
print("There is a door with a keypad on it.")
print("You need to enter the code to get out.")
print()

num = 0   # keeps track of which clue to show
guess = input("Enter the code: ")
while guess != code:
    print("Nope, thats not it.")
    if num < len(clues):
        print(clues[num])
        num += 1
    else:
        print("Out of clues, good luck lol")
    print()
    guess = input("Enter the code: ")

print()
print("The door opens!")
print("You escaped!")