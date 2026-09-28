# SI - Period 1 - User Sign In Assignment

# Predefined credentials stored in the program
CORRECT_USERNAME = "userone"
CORRECT_PASSWORD = "password"

# Loop until the user logs in successfully or gives up
while True:
    # Ask the user for their username and password
    # .strip() removes accidental spaces, .lower() fixes caps lock
    username = input("What is your username: ").strip().lower()
    password = input("What is your password: ").strip()

    # Complain about empty inputs before checking credentials
    if username == "" or password == "":
        print("You can't leave a field blank. Try again.\n")
        continue

    # Check BOTH username and password before welcoming
    if username == CORRECT_USERNAME and password == CORRECT_PASSWORD:
        print("\nWelcome to the program!")
        break  # Login successful, exit the loop
    else:
        print("Your login credentials were invalid.")
        # Let them quit instead of looping forever
        retry = input("Try again? (y/n): ").strip().lower()
        if retry != "y":
            print("Goodbye!")
            break
        print()  # blank line before the next attempt

