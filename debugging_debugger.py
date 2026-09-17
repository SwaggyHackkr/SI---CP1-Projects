# Ravager Snack Bar
import random

pirate_name = input("What's your name, pirate? ")
snack_name = input("What snack do you want? ")

price = random.randint(2, 8)  # random price in credits
quantity = int(input("How many would you like? "))

total = price * quantity

discounted_total = total  * 0.90


tax_rate = 0.08 #This tells us the tax rate
total_with_tax = discounted_total + (discounted_total * tax_rate)#This will give us the total with tax

print("Hello, " + pirate_name + "! Here's your order summary:")#Prints the pirates name + message of order summary
print("Snack: " + snack_name)# Tells user the snack + the snack name they chose
print("Price per snack: " + str(price) + " credits")# Tells us the price per snack 
print("Total before tax: " + str(total))#This tells us the price before the tax
print("Total with tax: " + str(round(total_with_tax, 2)) + " credits")#This is the price with tax 