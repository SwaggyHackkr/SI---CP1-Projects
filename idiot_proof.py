# Salesi Ilaoa, P1, Idiot proof assignment

name = input("What is your name: ").strip().title()

phone_number = float(input("What is your phone number: "))

gpa = float(input("What is your gpa: "))

print(f"Your name is {name} while your age is {phone_number} and you gpa is {gpa} ")


def gpa(prompt):
    while True:
        try:
             gpa = float(input(prompt))
             return gpa
        except ValueError:
                 print("Invalid input. Please enter a valid number for the gpa")


def phone_number(prompt):
      while True:
            try:
                  phone_number = float(input(prompt))
                  return phone_number
            except ValueError:
                  print("Invalid input, please enter a valid phone number")