# SI, Period 1,  Shopping List Manager

# Create an empty list to hold the shopping items
shopping_list = []

# Keep looping until the user chooses "exit"
while True:
    # Ask the user what they want to do
    action = input("What would you like to do? (add, remove, view, exit): ")

    if action == "add":
        # Get the item name from the user
        item = input("What item would you like to add? ")
        # Add the new item to the end of the list
        shopping_list.append(item)
        # Print the updated list so the user sees the result right away
        print("Your list:")
        for thing in shopping_list:
            # Loop through the list and print one item per line
            print(thing)
        # Print a blank line to separate this turn from the next
        print()

    elif action == "remove":
        # Get the item name the user wants to remove
        item = input("What item would you like to remove? ")
        # Only remove if the item is actually on the list, to avoid an error
        if item in shopping_list:
            shopping_list.remove(item)
        else:
            # Tell the user the item isn't there
            print("That item is not on your list.")
        # Print the updated list
        print("Your list:")
        for thing in shopping_list:
            print(thing)
        print()

    elif action == "view":
        # Just display the list without changing anything
        print("Your list:")
        for thing in shopping_list:
            print(thing)
        print()

    elif action == "exit":
        # Say goodbye and stop the loop, which ends the program
        print("Goodbye!")
        break

    else:
        # The user typed something that isn't a valid option
        print("Please type add, remove, view, or exit.")
        print()
