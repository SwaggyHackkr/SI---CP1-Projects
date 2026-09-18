# SI - Period 1 - Ravager Snack Bar Assignment

import random  # brings in the random module so we can generate a random price

pirate_name = input("What's your name, pirate? ")  # asks the pirate for their name and stores it as a string
snack_name = input("What snack do you want? ")  # asks which snack they want and stores it as a string

price = random.randint(2, 8)  # picks a random whole-number price between 2 and 8 credits
quantity = int(input("How many would you like? "))  # asks how many snacks, and converts the typed answer from a string to an integer

total = price * quantity  # multiplies price per snack by quantity to get the full price before discounts or tax

discounted_total = total * 0.90  # applies the 10% crew discount by charging only 90% of the total

tax_rate = 0.08  # sets the tax rate to 8% (written as a decimal)
total_with_tax = discounted_total + (discounted_total * tax_rate)  # adds 8% tax on top of the discounted total

print("Hello, " + pirate_name + "! Here's your order summary:")  # greets the pirate by name and starts the receipt
print("Snack: " + snack_name)  # displays which snack was ordered
print("Price per snack: " + str(price) + " credits")  # shows the random price of one snack (converts the number to a string to glue it into the text)
print("Total before tax: " + str(discounted_total) + " credits")  # shows the discounted total before tax is added
print("Total with tax: " + str(round(total_with_tax, 2)) + " credits")  # rounds the final total to 2 decimal places and displays it