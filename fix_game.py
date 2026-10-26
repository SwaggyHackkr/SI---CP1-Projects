# Salesi Ilaoa, Period: 1 , Assignment: Fix the Game
import random

scores = []
rounds = 3

print("Welcome to Guess the Number! You'll play 3 rounds.")
print("Each round, try to guess the number in as few tries as possible.\n")

for round_num in range(1, rounds + 1):
    secret_number = random.randint(1, 20)
    guesses = 0
    found = False

    print(f"--- Round {round_num} ---")

    while found == False:
        guess = int(input("Guess a number between 1 and 20: "))
        guesses = guesses + 1

        if guess == secret_number:  # bug 1 (Syntax): missing colon. Program wouldn't even start.
            print(f"Correct! It took you {guesses} guesses.")
            found = True
        elif guess < secret_number:
            print("Too low!")
        elif guess > secret_number:
            print("Too high!")

    scores.append(guesses)

print("\n--- Game Over ---")

print(f"Your guesses per round: {scores}")  # bug 2 (Runtime): str + list crashes with TypeError at game over.

total = 0
for score in scores:
    total = total + score  # bug 3 (Logic): "total = 0" was inside loop, resetting it. Average was wrong.

average = total / rounds
print("Your average guesses per round was " + str(average))

best_round = scores[0]
for i in range(1, rounds):  # bug 4 (Logic): was rounds - 1, so the last round was never checked for best.
    if scores[i] < best_round:
        best_round = scores[i]

print(f"Your best round took only {best_round} guesses!")