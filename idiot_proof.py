#Salesi Ilaoa, Period 1, idiot proof assignment

# Try and except blocks to validate user input for name,

while True:
    try:
        name = input("What is your name?: ")
        if not name.replace(" ", "").isalpha():
            raise ValueError
        break
    except ValueError:
        print("Please enter a valid name (letters only).")


# Format: capitalize the first letter of each word in the name, rest lowercase

words = name.split()
formatted_name =""
for word in words:
    formatted_name += word[0].upper() + word[1:].lower() + " "
formatted_name = formatted_name.strip()


#Try and except blocks to validate user input for phone number

while True:
    try:
        phone_number = input("What is your phone number?: ")
        digits = phone_number.replace("-", "").replace(" ", "")
        if not digits.isdigit() or len(digits) != 10:
            raise ValueError
        break
    except ValueError:
        print("Please enter a valid phone number (10 digits, numbers only).")

# Format: 000 000 0000
formatted_phone = digits[:3] + " " + digits[3:6] + " " + digits[6:]


#Try and except blocks to validate user input for GPA

while True:
    try:
        gpa = float(input("What is your GPA?: "))
        if gpa < 0.0 or gpa > 4.0:
            raise ValueError
        break
    except ValueError:
        print("Please enter a valid GPA (between 0.0 and 4.0).")

formatted_gpa = round(gpa, 1)

# The final output of the program will be the formatted name, phone number, and GPA printed to the console.

print()
print("Name:", formatted_name)
print("Phone Number:", formatted_phone)
print("GPA:", str(formatted_gpa))